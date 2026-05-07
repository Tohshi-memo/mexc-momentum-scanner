# Decision Report

- generated_at: 2026-05-07T21:57:40.101361+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3709**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3709, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-1.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.04% | **-1.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_BB3S | 4/19 | 21.1% | +1.13% | **+0.24%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.97% | **+1.97%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +2.72% | **+1.09%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.10% | **+1.05%** |
| ASK_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +4.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$99.82** / 初期 $100.00 (-0.18%)
- 確定トレード: 22件 (TP 6 / SL 14 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.82
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 189件 (Win 48 / Loss 64 / Flat 77) / skip 81件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +3.48%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FHE/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-07T21:57:36.195975+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=79738.5
- Funnel: target 765 → liquid 186 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 97.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +55.99% | $7,268,186.98 |
| NIL/USDT:USDT | +38.24% | $16,584,228.80 |
| TST/USDT:USDT | +24.05% | $5,707,087.46 |
| DYDX/USDT:USDT | +18.29% | $9,457,324.01 |
| NOT/USDT:USDT | +14.12% | $10,232,594.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DYDX/USDT:USDT | below_1h_threshold | +3.03% | +3.16% |
| STRK/USDT:USDT | below_1h_threshold | +2.81% | +2.93% |
| XPL/USDT:USDT | below_1h_threshold | +2.75% | +2.87% |
| BSB/USDT:USDT | below_1h_threshold | +2.06% | +2.19% |
| LAB/USDT:USDT | below_1h_threshold | +1.95% | +2.08% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
