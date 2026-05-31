# Decision Report

- generated_at: 2026-05-31T19:41:33.731129+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5219**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5219, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.92% | **-1.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +1.92% | **+0.77%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.16% | **+0.58%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.36% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +4.00% | **+4.00%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +4.39% | **+2.85%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +3.98% | **+2.59%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +4.20% | **+2.31%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +4.03% | **+2.02%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.82** / 初期 $100.00 (+31.82%)
- 確定: 854件 (Win 199 / Loss 254 / Flat 401) / skip 926件
- 成長率目線: 平均log +0.000323 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: XLM/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $131.82

## 4. Latest Market Context

- 更新: 2026-05-31T19:41:30.342473+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=73496.6
- Funnel: target 773 → liquid 129 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.4 >= 65=1, 4h RSI 66.2 >= 65=1, 4h RSI 70.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +41.88% | $13,224,840.86 |
| ZORA/USDT:USDT | +16.01% | $1,126,914.40 |
| BSB/USDT:USDT | +9.99% | $4,794,428.35 |
| UB/USDT:USDT | +9.74% | $6,911,396.67 |
| HOME/USDT:USDT | +9.07% | $2,573,457.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZORA/USDT:USDT | below_1h_threshold | +4.42% | +4.53% |
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +4.17% | +4.28% |
| UB/USDT:USDT | below_1h_threshold | +2.17% | +2.27% |
| PORTAL/USDT:USDT | below_1h_threshold | +1.59% | +1.70% |
| FET/USDT:USDT | below_1h_threshold | +1.46% | +1.57% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
