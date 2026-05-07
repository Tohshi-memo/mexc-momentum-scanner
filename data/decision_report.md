# Decision Report

- generated_at: 2026-05-07T21:47:46.155252+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3706**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3706, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.44% | **-0.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/19 | 21.1% | +2.53% | **+0.53%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.60% | **+0.24%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.37% | **+1.37%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +1.97% | **+0.49%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.90% | **+0.45%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |
| ASK_LONG | 20/20 | 100.0% | +0.36% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$99.82** / 初期 $100.00 (-0.18%)
- 確定トレード: 22件 (TP 6 / SL 14 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.82
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 189件 (Win 48 / Loss 64 / Flat 77) / skip 78件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +3.48%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FHE/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-07T21:47:42.573955+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=79790.1
- Funnel: target 765 → liquid 185 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.0 >= 65=1, 4h RSI 96.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +66.65% | $7,096,656.84 |
| NIL/USDT:USDT | +37.98% | $15,510,266.05 |
| TST/USDT:USDT | +25.08% | $5,625,763.68 |
| DYDX/USDT:USDT | +16.55% | $9,315,721.04 |
| NOT/USDT:USDT | +15.12% | $10,220,841.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STRK/USDT:USDT | below_1h_threshold | +3.30% | +3.36% |
| LAB/USDT:USDT | below_1h_threshold | +3.30% | +3.36% |
| XPL/USDT:USDT | below_1h_threshold | +2.94% | +3.00% |
| LINEA/USDT:USDT | below_1h_threshold | +2.12% | +2.18% |
| HIGH/USDT:USDT | below_1h_threshold | +1.91% | +1.97% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
