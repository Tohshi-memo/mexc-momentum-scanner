# Decision Report

- generated_at: 2026-05-11T13:57:28.082641+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4034**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4034, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-1.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.33% | **-1.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_3PCT | 19/20 | 95.0% | +0.71% | **+0.68%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.22% | **-0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +3.46% | **+1.04%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.59% | **+0.95%** |
| MARKET_LONG | 20/20 | 100.0% | +0.90% | **+0.90%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +4.00% | **+0.80%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +1.62% | **+0.65%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 33件 (TP 8 / SL 22 / EXP 3)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 377件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T13:57:25.150417+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=81018.4
- Funnel: target 762 → liquid 187 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.2 >= 65=1, 4h RSI 74.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TROLLSOL/USDT:USDT | +39.59% | $4,498,912.66 |
| US/USDT:USDT | +38.97% | $14,447,126.87 |
| PENGUIN/USDT:USDT | +29.72% | $1,728,543.99 |
| SAGA/USDT:USDT | +25.58% | $3,688,021.48 |
| B/USDT:USDT | +20.32% | $13,032,088.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STXSTOCK/USDT:USDT | below_1h_threshold | +4.11% | +4.10% |
| FF/USDT:USDT | below_1h_threshold | +3.46% | +3.46% |
| JELLYJELLY/USDT:USDT | below_1h_threshold | +3.27% | +3.26% |
| PLAY/USDT:USDT | below_1h_threshold | +2.75% | +2.75% |
| SILVER/USDT:USDT | below_1h_threshold | +2.44% | +2.43% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
