# Decision Report

- generated_at: 2026-09-02T02:41:49.961505+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13290**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13290, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 7/20 | 35.0% | +4.44% | **+1.56%** |
| LIMIT_6PCT | 10/20 | 50.0% | +1.34% | **+0.67%** |
| LIMIT_9PCT | 4/20 | 20.0% | +3.29% | **+0.66%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_7PCT | 7/20 | 35.0% | +1.60% | **+0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +7.04% | **+5.63%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +2.92% | **+2.62%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +4.73% | **+2.60%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +2.01% | **+2.01%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +4.19% | **+1.88%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 197件 (TP 73 / SL 119 / EXP 5)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$841.34** / 初期 $100.00 (+741.34%)
- 確定: 4925件 (Win 1502 / Loss 1621 / Flat 1802) / skip 4926件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEMI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $841.34

## 4. Robust Adaptive DryRun ($100)

- 残高: **$175.81** / 初期 $100.00 (+75.81%)
- 確定: 2269件 (Win 635 / Loss 545 / Flat 1089) / skip 4432件
- 成長率目線: 平均log +0.000249 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1294 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $175.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.88** / 初期 $100.00 (+14.88%)
- 確定: 2089件 (Win 610 / Loss 817 / Flat 662) / pending 0件 / skip 2673件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000353 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FILECOIN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.88

## 6. Latest Market Context

- 更新: 2026-09-02T02:41:35.007609+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=77170.0
- Funnel: target 1036 → liquid 159 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEMI/USDT:USDT | +27.62% | $6,059,195.94 |
| MAGMA/USDT:USDT | +26.49% | $4,993,474.39 |
| UAI/USDT:USDT | +25.99% | $17,942,849.32 |
| FONE/USDT:USDT | +14.10% | $1,385,471.97 |
| CASHCAT/USDT:USDT | +13.05% | $1,228,227.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BONER/USDT:USDT | below_1h_threshold | +4.26% | +4.02% |
| ZRO/USDT:USDT | below_1h_threshold | +2.60% | +2.36% |
| AR/USDT:USDT | below_1h_threshold | +2.51% | +2.27% |
| FONE/USDT:USDT | below_1h_threshold | +2.49% | +2.25% |
| PENDLE/USDT:USDT | below_1h_threshold | +1.95% | +1.71% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
