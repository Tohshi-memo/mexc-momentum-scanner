# Decision Report

- generated_at: 2026-09-04T08:41:22.719208+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13594**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.66% / filled 20/20。**
- 全期間 MARKET基準: n=13594, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +1.08% | **+0.98%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.76% | **+0.72%** |
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.83% | **+0.62%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.59% | **+0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.19% | **+0.48%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.59% | **+0.41%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5009件 (Win 1516 / Loss 1644 / Flat 1849) / skip 5146件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.90** / 初期 $100.00 (+85.90%)
- 確定: 2409件 (Win 681 / Loss 576 / Flat 1152) / skip 4596件
- 成長率目線: 平均log +0.000257 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0218 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $185.90

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.02** / 初期 $100.00 (+16.02%)
- 確定: 2247件 (Win 667 / Loss 878 / Flat 702) / pending 3件 / skip 2814件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000089 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.04% 残高後 $116.02

## 6. Latest Market Context

- 更新: 2026-09-04T08:41:13.228538+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.52% price=81049.0
- Funnel: target 1051 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TRIA/USDT:USDT | +35.69% | $5,869,746.76 |
| USELESS/USDT:USDT | +35.42% | $33,876,219.94 |
| HNT/USDT:USDT | +16.43% | $13,110,974.45 |
| PROM/USDT:USDT | +16.05% | $2,588,432.50 |
| ZEST/USDT:USDT | +11.14% | $1,210,032.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPX/USDT:USDT | below_relative_strength | +5.16% | +4.64% |
| USELESS/USDT:USDT | below_1h_threshold | +4.11% | +3.59% |
| DASH/USDT:USDT | below_1h_threshold | +2.95% | +2.43% |
| PROM/USDT:USDT | below_1h_threshold | +2.67% | +2.15% |
| LIT/USDT:USDT | below_1h_threshold | +2.61% | +2.09% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
