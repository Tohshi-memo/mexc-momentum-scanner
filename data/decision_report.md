# Decision Report

- generated_at: 2026-08-29T10:11:19.701559+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12922**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.79% / filled 20/20。**
- 全期間 MARKET基準: n=12922, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.79% | **+0.79%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.79% | **+0.75%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.63% | **+0.41%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.35% | **+0.31%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.45% | **+0.29%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.56% | **+0.22%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.18% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$710.55** / 初期 $100.00 (+610.55%)
- 確定: 4692件 (Win 1419 / Loss 1542 / Flat 1731) / skip 4791件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TOAD/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $710.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.75** / 初期 $100.00 (+56.75%)
- 確定: 2007件 (Win 546 / Loss 485 / Flat 976) / skip 4326件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0173 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HNT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $156.75

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.70** / 初期 $100.00 (+16.70%)
- 確定: 2017件 (Win 593 / Loss 778 / Flat 646) / pending 2件 / skip 2372件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000372 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TOAD/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $116.70

## 6. Latest Market Context

- 更新: 2026-08-29T10:11:08.790371+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=77525.9
- Funnel: target 1023 → liquid 141 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TOAD/USDT:USDT | +97.47% | $1,738,632.22 |
| HNT/USDT:USDT | +62.81% | $3,890,092.46 |
| O/USDT:USDT | +20.03% | $1,227,772.58 |
| ONG/USDT:USDT | +16.09% | $4,067,631.91 |
| COTI/USDT:USDT | +15.39% | $1,476,033.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTR/USDT:USDT | below_1h_threshold | +3.47% | +3.59% |
| LONGXIA/USDT:USDT | below_1h_threshold | +2.42% | +2.54% |
| TUT/USDT:USDT | below_1h_threshold | +1.16% | +1.28% |
| MAGMA/USDT:USDT | below_1h_threshold | +0.59% | +0.71% |
| DOS/USDT:USDT | below_1h_threshold | +0.51% | +0.63% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
