# Decision Report

- generated_at: 2026-09-05T01:26:20.269978+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13679**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.28% / filled 20/20。**
- 全期間 MARKET基準: n=13679, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| MARKET | 20/20 | 100.0% | +0.28% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.19% | **+0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.41% | **+1.36%** |
| MARKET_LONG | 20/20 | 100.0% | +1.12% | **+1.12%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.40% | **+1.05%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.17% | **+0.94%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 202件 (TP 75 / SL 122 / EXP 5)
- 最新: AKE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$855.36** / 初期 $100.00 (+755.36%)
- 確定: 5012件 (Win 1516 / Loss 1645 / Flat 1851) / skip 5228件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 4/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $855.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.52** / 初期 $100.00 (+85.52%)
- 確定: 2427件 (Win 683 / Loss 578 / Flat 1166) / skip 4663件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0707 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $185.52

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.14** / 初期 $100.00 (+18.14%)
- 確定: 2313件 (Win 689 / Loss 887 / Flat 737) / pending 3件 / skip 2834件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000270 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $118.14

## 6. Latest Market Context

- 更新: 2026-09-05T01:26:10.281507+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=79611.0
- Funnel: target 1050 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4/USDT:USDT | +53.89% | $11,969,974.06 |
| DASH/USDT:USDT | +23.76% | $30,839,111.33 |
| USELESS/USDT:USDT | +20.11% | $45,200,654.55 |
| BASECAT/USDT:USDT | +19.88% | $1,998,340.66 |
| ZEN/USDT:USDT | +15.63% | $7,085,781.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CYS/USDT:USDT | below_1h_threshold | +2.89% | +2.80% |
| CHIP/USDT:USDT | below_1h_threshold | +2.42% | +2.33% |
| USELESS/USDT:USDT | below_1h_threshold | +2.25% | +2.16% |
| ORDI/USDT:USDT | below_1h_threshold | +1.11% | +1.02% |
| ZEN/USDT:USDT | below_1h_threshold | +0.98% | +0.90% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
