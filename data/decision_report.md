# Decision Report

- generated_at: 2026-09-23T17:36:27.411354+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15440**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.07% / filled 20/20。**
- 全期間 MARKET基準: n=15440, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.07% | **+2.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +2.97% | **+2.38%** |
| MARKET | 20/20 | 100.0% | +2.07% | **+2.07%** |
| LIMIT_3PCT | 14/20 | 70.0% | +2.75% | **+1.92%** |
| LIMIT_5PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_ATR | 13/20 | 65.0% | +2.43% | **+1.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +2.40% | **+1.20%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +1.83% | **+1.10%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | -0.59% | **-0.36%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | -0.78% | **-0.47%** |

## 2. $100 Live Portfolio

- 残高: **$120.32** / 初期 $100.00 (+20.32%)
- 確定トレード: 217件 (TP 79 / SL 133 / EXP 5)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5896件 (Win 1739 / Loss 1890 / Flat 2267) / skip 6105件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$252.39** / 初期 $100.00 (+152.39%)
- 確定: 3387件 (Win 933 / Loss 790 / Flat 1664) / skip 5464件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0630 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAKE/USDT:USDT `LIMIT_5PCT` TP_HIT account +0.69% 残高後 $252.39

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.57** / 初期 $100.00 (+21.57%)
- 確定: 3136件 (Win 923 / Loss 1234 / Flat 979) / pending 0件 / skip 3775件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000252 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GRASS/USDT:USDT `MARKET` EXPIRED account -0.14% 残高後 $121.57

## 6. Latest Market Context

- 更新: 2026-09-23T17:36:13.854561+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=83956.7
- Funnel: target 1061 → liquid 194 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAKE/USDT:USDT | +14.08% | $12,238,361.66 |
| MARSCOIN/USDT:USDT | +11.62% | $3,700,326.76 |
| FIGHT/USDT:USDT | +5.94% | $1,171,898.08 |
| PENDLE/USDT:USDT | +5.17% | $2,667,654.62 |
| BSV/USDT:USDT | +4.19% | $3,817,512.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COTI/USDT:USDT | below_1h_threshold | +1.98% | +2.03% |
| ZRO/USDT:USDT | below_1h_threshold | +1.93% | +1.98% |
| ON/USDT:USDT | below_1h_threshold | +1.79% | +1.84% |
| AKE/USDT:USDT | below_1h_threshold | +1.71% | +1.75% |
| BEAT/USDT:USDT | below_1h_threshold | +1.67% | +1.72% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
