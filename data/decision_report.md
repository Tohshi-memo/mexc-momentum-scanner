# Decision Report

- generated_at: 2026-05-07T13:22:43.663227+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3632**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3632, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.35% | **-0.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_8PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.27% | **+0.68%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +5.95% | **+2.38%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +3.40% | **+1.87%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.78% | **+1.53%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.58% | **+1.43%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +4.00% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$100.83** / 初期 $100.00 (+0.83%)
- 確定トレード: 20件 (TP 6 / SL 12 / EXP 2)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$109.90** / 初期 $100.00 (+9.90%)
- 確定: 126件 (Win 41 / Loss 48 / Flat 37) / skip 67件
- 成長率目線: 平均log +0.000750 / 幾何平均 +0.075% per trade / maxDD +2.62%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_7PCT_LONG` TP_HIT account +1.00% 残高後 $109.90

## 4. Latest Market Context

- 更新: 2026-05-07T13:22:40.304327+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=81056.7
- Funnel: target 771 → liquid 181 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +99.15% | $2,960,734.04 |
| B3/USDT:USDT | +90.55% | $11,532,396.47 |
| PENGUIN/USDT:USDT | +78.09% | $3,979,732.19 |
| DOGS/USDT:USDT | +52.85% | $16,953,529.08 |
| SIREN/USDT:USDT | +40.66% | $19,891,199.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SIREN/USDT:USDT | below_1h_threshold | +4.79% | +4.86% |
| FHE/USDT:USDT | below_1h_threshold | +4.66% | +4.74% |
| PENGUIN/USDT:USDT | below_1h_threshold | +4.21% | +4.29% |
| HMSTR/USDT:USDT | below_1h_threshold | +2.86% | +2.94% |
| XPL/USDT:USDT | below_1h_threshold | +2.67% | +2.75% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
