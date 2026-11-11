# Decision Report

- generated_at: 2026-11-11T19:41:34.387659+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18697**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18697, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.52%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.52% | **-1.52%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/20 | 25.0% | +2.90% | **+0.73%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.32% | **+0.53%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.53% | **+0.40%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.85% | **+2.57%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.80% | **+1.68%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.32% | **+1.62%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| MARKET_LONG | 20/20 | 100.0% | +0.92% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$120.89** / 初期 $100.00 (+20.89%)
- 確定トレード: 270件 (TP 97 / SL 165 / EXP 8)
- 最新: SNXX/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.89
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,743.00** / 初期 $100.00 (+1643.00%)
- 確定: 7229件 (Win 2083 / Loss 2312 / Flat 2834) / skip 8029件
- 成長率目線: 平均log +0.000395 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FLOAT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,743.00

## 4. Robust Adaptive DryRun ($100)

- 残高: **$390.28** / 初期 $100.00 (+290.28%)
- 確定: 4779件 (Win 1283 / Loss 1057 / Flat 2439) / skip 7329件
- 成長率目線: 平均log +0.000285 / 幾何平均 +0.028% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1440 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AGT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $390.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6866件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000161 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-11T19:41:20.523653+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=74353.3
- Funnel: target 1103 → liquid 147 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIN/USDT:USDT | +15.30% | $1,215,566.28 |
| Q/USDT:USDT | +12.77% | $2,464,816.47 |
| ARIA/USDT:USDT | +9.48% | $9,637,787.17 |
| AGT/USDT:USDT | +3.18% | $31,517,246.72 |
| ETHFI/USDT:USDT | +2.90% | $3,107,989.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIN/USDT:USDT | below_1h_threshold | +1.39% | +1.53% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +1.16% | +1.30% |
| Q/USDT:USDT | below_1h_threshold | +1.15% | +1.28% |
| AGT/USDT:USDT | below_1h_threshold | +1.13% | +1.27% |
| ZRO/USDT:USDT | below_1h_threshold | +1.12% | +1.25% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
