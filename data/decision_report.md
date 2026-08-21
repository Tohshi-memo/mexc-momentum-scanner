# Decision Report

- generated_at: 2026-08-21T20:21:20.880222+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12250**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.53% / filled 20/20。**
- 全期間 MARKET基準: n=12250, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.53%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.53% | **+0.53%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 8/16 | 50.0% | +1.91% | **+0.95%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.96% | **+0.59%** |
| MARKET | 20/20 | 100.0% | +0.53% | **+0.53%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.63% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.57% | **+0.79%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.51% | **+0.46%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.10% | **+0.38%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$643.52** / 初期 $100.00 (+543.52%)
- 確定: 4374件 (Win 1338 / Loss 1435 / Flat 1601) / skip 4437件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGMA/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $643.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.44** / 初期 $100.00 (+55.44%)
- 確定: 1859件 (Win 513 / Loss 443 / Flat 903) / skip 3802件
- 成長率目線: 平均log +0.000237 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0313 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MAGMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $155.44

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.90** / 初期 $100.00 (+16.90%)
- 確定: 1824件 (Win 540 / Loss 693 / Flat 591) / pending 0件 / skip 1901件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000174 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `MARKET_LONG` EXPIRED account -0.09% 残高後 $116.90

## 6. Latest Market Context

- 更新: 2026-08-21T20:21:12.196711+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.50% price=77379.9
- Funnel: target 1018 → liquid 217 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=2, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +168.04% | $1,845,742.96 |
| CATE/USDT:USDT | +35.36% | $11,072,239.98 |
| JIMOTHY/USDT:USDT | +33.98% | $1,436,863.46 |
| COTI/USDT:USDT | +20.78% | $2,769,198.91 |
| MAGMA/USDT:USDT | +10.88% | $1,619,375.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEC/USDT:USDT | below_relative_strength | +5.22% | +4.72% |
| MAGMA/USDT:USDT | below_relative_strength | +5.05% | +4.55% |
| COTI/USDT:USDT | below_1h_threshold | +4.49% | +3.99% |
| ROBO/USDT:USDT | below_1h_threshold | +3.54% | +3.04% |
| NIULAI/USDT:USDT | below_1h_threshold | +2.96% | +2.46% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
