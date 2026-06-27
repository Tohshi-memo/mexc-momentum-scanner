# Decision Report

- generated_at: 2026-06-27T02:42:09.742167+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7667**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7667, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.99% | **-1.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_BB3S | 4/17 | 23.5% | +0.03% | **+0.01%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.23% | **-0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.28% | **+1.80%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.79% | **+1.53%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.66% | **+1.46%** |
| LIMIT_4PCT_LONG | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.51% | **+1.06%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$236.95** / 初期 $100.00 (+136.95%)
- 確定: 2192件 (Win 656 / Loss 729 / Flat 807) / skip 2036件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $236.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.98** / 初期 $100.00 (+7.98%)
- 確定: 398件 (Win 108 / Loss 100 / Flat 190) / skip 680件
- 成長率目線: 平均log +0.000193 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0399 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $107.98

## 5. Latest Market Context

- 更新: 2026-06-27T02:42:03.132906+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.60% price=60285.4
- Funnel: target 806 → liquid 162 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PUNDIX/USDT:USDT | +47.31% | $4,616,993.36 |
| MYX/USDT:USDT | +26.38% | $3,035,813.09 |
| VELVET/USDT:USDT | +22.64% | $32,071,456.23 |
| AGLD/USDT:USDT | +16.04% | $7,287,181.62 |
| SLX/USDT:USDT | +15.48% | $11,120,669.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| O/USDT:USDT | below_relative_strength | +5.27% | +4.67% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.74% | +3.14% |
| BEAT/USDT:USDT | below_1h_threshold | +3.74% | +3.13% |
| RE/USDT:USDT | below_1h_threshold | +3.51% | +2.91% |
| ARX/USDT:USDT | below_1h_threshold | +3.39% | +2.78% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
