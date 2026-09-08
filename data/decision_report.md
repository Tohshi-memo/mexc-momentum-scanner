# Decision Report

- generated_at: 2026-09-08T12:56:20.371431+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13987**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.60% / filled 20/20。**
- 全期間 MARKET基準: n=13987, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.60% | **+1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.84% | **+0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.04% | **+0.02%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | -0.60% | **-0.18%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | -0.71% | **-0.42%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -2.28% | **-0.57%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,007.04** / 初期 $100.00 (+907.04%)
- 確定: 5251件 (Win 1584 / Loss 1707 / Flat 1960) / skip 5297件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: G/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $1,007.04

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.03** / 初期 $100.00 (+90.03%)
- 確定: 2590件 (Win 722 / Loss 622 / Flat 1246) / skip 4808件
- 成長率目線: 平均log +0.000248 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0727 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: G/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $190.03

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.23** / 初期 $100.00 (+21.23%)
- 確定: 2576件 (Win 756 / Loss 970 / Flat 850) / pending 3件 / skip 2878件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000132 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: G/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $121.23

## 6. Latest Market Context

- 更新: 2026-09-08T12:56:10.263872+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=78413.7
- Funnel: target 1070 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOPH/USDT:USDT | +58.09% | $26,148,147.69 |
| BNCSTOCK/USDT:USDT | +38.81% | $1,994,169.59 |
| FORM/USDT:USDT | +21.94% | $4,504,294.91 |
| MEMEROBINHOOD/USDT:USDT | +17.72% | $5,590,753.20 |
| AKE/USDT:USDT | +16.27% | $10,778,125.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VVV/USDT:USDT | below_1h_threshold | +3.76% | +3.75% |
| ATOM/USDT:USDT | below_1h_threshold | +3.12% | +3.11% |
| CHIP/USDT:USDT | below_1h_threshold | +2.91% | +2.89% |
| PONS/USDT:USDT | below_1h_threshold | +2.89% | +2.88% |
| ETC/USDT:USDT | below_1h_threshold | +2.51% | +2.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
