# Decision Report

- generated_at: 2026-08-05T05:36:35.673286+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10367**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.23% / filled 20/20。**
- 全期間 MARKET基準: n=10367, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.23% | **+0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| MARKET | 20/20 | 100.0% | +0.23% | **+0.23%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 8/9 | 88.9% | +3.85% | **+3.42%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.06% | **+1.85%** |
| MARKET_LONG | 20/20 | 100.0% | +1.44% | **+1.44%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.01% | **+0.65%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.78% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$617.61** / 初期 $100.00 (+517.61%)
- 確定: 3762件 (Win 1194 / Loss 1230 / Flat 1338) / skip 3166件
- 成長率目線: 平均log +0.000484 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HFT/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.62% 残高後 $617.61

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.20** / 初期 $100.00 (+43.20%)
- 確定: 1301件 (Win 366 / Loss 303 / Flat 632) / skip 2477件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1113 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HFT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $143.20

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.01** / 初期 $100.00 (+19.01%)
- 確定: 1117件 (Win 360 / Loss 430 / Flat 327) / pending 6件 / skip 719件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000408 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HFT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $119.01

## 6. Latest Market Context

- 更新: 2026-08-05T05:36:24.808166+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.30% price=64330.9
- Funnel: target 939 → liquid 185 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.5 >= 65=1, 4h RSI 84.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +95.25% | $11,166,843.06 |
| HFT/USDT:USDT | +63.23% | $1,381,824.83 |
| BLESS/USDT:USDT | +48.14% | $24,463,941.31 |
| BICO/USDT:USDT | +38.23% | $15,686,872.90 |
| TAKE/USDT:USDT | +36.80% | $1,607,959.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRVT/USDT:USDT | below_relative_strength | +5.19% | +4.89% |
| TUT/USDT:USDT | below_1h_threshold | +3.61% | +3.31% |
| HEI/USDT:USDT | below_1h_threshold | +2.99% | +2.70% |
| KAITO/USDT:USDT | below_1h_threshold | +2.66% | +2.37% |
| SNXX/USDT:USDT | below_1h_threshold | +2.20% | +1.91% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
