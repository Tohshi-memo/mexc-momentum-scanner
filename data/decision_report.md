# Decision Report

- generated_at: 2026-05-11T14:28:05.933693+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4040**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4040, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-1.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.35% | **-1.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.52% | **+0.88%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.92% | **+0.67%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.17% | **+1.41%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.81% | **+1.09%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +1.07% | **+1.07%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.33% | **+1.05%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +3.46% | **+1.04%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 33件 (TP 8 / SL 22 / EXP 3)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 383件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T14:28:01.231031+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=80837.5
- Funnel: target 762 → liquid 184 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.3 >= 65=1, 4h RSI 84.9 >= 65=1, 4h RSI 83.5 >= 65=1, 4h RSI 72.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +50.83% | $15,577,578.30 |
| TROLLSOL/USDT:USDT | +48.98% | $4,677,245.91 |
| US/USDT:USDT | +39.13% | $14,732,049.12 |
| PENGUIN/USDT:USDT | +36.89% | $1,832,531.37 |
| SAGA/USDT:USDT | +34.28% | $3,935,052.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRUTH/USDT:USDT | below_1h_threshold | +1.57% | +1.81% |
| KAS/USDT:USDT | below_1h_threshold | +1.11% | +1.35% |
| PARTI/USDT:USDT | below_1h_threshold | +1.08% | +1.32% |
| STXSTOCK/USDT:USDT | below_1h_threshold | +1.02% | +1.26% |
| BRETT/USDT:USDT | below_1h_threshold | +0.90% | +1.14% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
