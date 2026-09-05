# Decision Report

- generated_at: 2026-09-05T06:21:38.299280+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13702**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13702, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.88% | **-1.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 9/20 | 45.0% | +4.18% | **+1.88%** |
| LIMIT_9PCT | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_8PCT | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.96% | **+0.88%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.57% | **+1.02%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.60% | **+0.72%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.83% | **+0.41%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.34% | **+0.29%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +0.80% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 203件 (TP 75 / SL 123 / EXP 5)
- 最新: NIULAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$858.36** / 初期 $100.00 (+758.36%)
- 確定: 5013件 (Win 1517 / Loss 1645 / Flat 1851) / skip 5250件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_7PCT` SL_HIT account +0.35% 残高後 $858.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$188.58** / 初期 $100.00 (+88.58%)
- 確定: 2449件 (Win 692 / Loss 585 / Flat 1172) / skip 4664件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0731 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $188.58

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.13** / 初期 $100.00 (+18.13%)
- 確定: 2335件 (Win 697 / Loss 897 / Flat 741) / pending 6件 / skip 2836件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000314 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_7PCT` SL_HIT account +0.12% 残高後 $118.13

## 6. Latest Market Context

- 更新: 2026-09-05T06:21:25.606913+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=79582.5
- Funnel: target 1050 → liquid 158 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +118.68% | $7,671,484.11 |
| 4/USDT:USDT | +63.81% | $15,766,035.99 |
| DASH/USDT:USDT | +37.54% | $42,516,586.39 |
| ZEN/USDT:USDT | +28.33% | $10,202,894.61 |
| AKE/USDT:USDT | +20.87% | $12,192,291.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TUT/USDT:USDT | below_1h_threshold | +3.54% | +3.49% |
| BULLA/USDT:USDT | below_1h_threshold | +1.71% | +1.66% |
| FLOKI/USDT:USDT | below_1h_threshold | +1.62% | +1.56% |
| LTC/USDT:USDT | below_1h_threshold | +1.54% | +1.48% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +1.46% | +1.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
