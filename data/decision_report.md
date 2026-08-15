# Decision Report

- generated_at: 2026-08-15T03:41:29.149015+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11629**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.04% / filled 20/20。**
- 全期間 MARKET基準: n=11629, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.04% | **+1.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.19% | **+1.08%** |
| MARKET | 20/20 | 100.0% | +1.04% | **+1.04%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.31% | **+0.66%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +0.55% | **+0.55%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.14% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$639.39** / 初期 $100.00 (+539.39%)
- 確定: 4097件 (Win 1284 / Loss 1350 / Flat 1463) / skip 4093件
- 成長率目線: 平均log +0.000453 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GRVT/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $639.39

## 4. Robust Adaptive DryRun ($100)

- 残高: **$152.49** / 初期 $100.00 (+52.49%)
- 確定: 1692件 (Win 483 / Loss 409 / Flat 800) / skip 3348件
- 成長率目線: 平均log +0.000249 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0350 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GRVT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $152.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.31** / 初期 $100.00 (+17.31%)
- 確定: 1575件 (Win 479 / Loss 604 / Flat 492) / pending 4件 / skip 1522件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000163 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ROBO/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $117.31

## 6. Latest Market Context

- 更新: 2026-08-15T03:41:19.003157+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=63039.4
- Funnel: target 985 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROBO/USDT:USDT | +27.07% | $2,635,137.99 |
| CYS/USDT:USDT | +15.32% | $15,992,214.37 |
| VELVET/USDT:USDT | +15.31% | $45,377,876.42 |
| US/USDT:USDT | +14.92% | $6,821,027.87 |
| AIO/USDT:USDT | +13.97% | $1,370,518.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +4.32% | +4.44% |
| ONE/USDT:USDT | below_1h_threshold | +3.28% | +3.40% |
| ROBO/USDT:USDT | below_1h_threshold | +2.39% | +2.50% |
| NIL/USDT:USDT | below_1h_threshold | +2.25% | +2.36% |
| HEI/USDT:USDT | below_1h_threshold | +2.19% | +2.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
