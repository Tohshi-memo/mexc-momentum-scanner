# Decision Report

- generated_at: 2026-10-01T17:21:35.148882+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15926**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.58% / filled 20/20。**
- 全期間 MARKET基準: n=15926, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.58% | **+0.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +5.92% | **+1.48%** |
| LIMIT_6PCT | 5/20 | 25.0% | +4.33% | **+1.08%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| MARKET | 20/20 | 100.0% | +0.58% | **+0.58%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.28% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.66% | **+1.25%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.20% | **+0.84%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.38% | **+0.36%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.40% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$120.63** / 初期 $100.00 (+20.63%)
- 確定トレード: 226件 (TP 82 / SL 137 / EXP 7)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.63
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,279.94** / 初期 $100.00 (+1179.94%)
- 確定: 6035件 (Win 1787 / Loss 1945 / Flat 2303) / skip 6452件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MOVR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,279.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$275.51** / 初期 $100.00 (+175.51%)
- 確定: 3579件 (Win 996 / Loss 829 / Flat 1754) / skip 5758件
- 成長率目線: 平均log +0.000283 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1173 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MOVR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $275.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4090件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000276 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T17:21:19.247667+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.70% price=84755.0
- Funnel: target 1097 → liquid 171 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +6.00% | $1,493,175.62 |
| SNXX/USDT:USDT | +4.54% | $5,476,003.47 |
| ZRO/USDT:USDT | +4.23% | $4,650,167.46 |
| SI/USDT:USDT | +3.78% | $6,326,616.48 |
| ARK/USDT:USDT | +3.77% | $7,529,908.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WIF/USDT:USDT | below_1h_threshold | +4.14% | +3.44% |
| LONGXIA/USDT:USDT | below_1h_threshold | +3.41% | +2.71% |
| CAP/USDT:USDT | below_1h_threshold | +3.19% | +2.49% |
| USELESS/USDT:USDT | below_1h_threshold | +3.06% | +2.36% |
| ZRO/USDT:USDT | below_1h_threshold | +3.03% | +2.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
