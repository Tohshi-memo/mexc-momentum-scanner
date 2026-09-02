# Decision Report

- generated_at: 2026-09-02T03:16:23.517008+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13294**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13294, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +4.74% | **+1.19%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_5PCT | 13/20 | 65.0% | +0.89% | **+0.58%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.21% | **+0.48%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/7 | 85.7% | +4.80% | **+4.11%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.28% | **+1.82%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.20% | **+1.60%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.54% | **+1.46%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.47% | **+1.36%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 197件 (TP 73 / SL 119 / EXP 5)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$832.95** / 初期 $100.00 (+732.95%)
- 確定: 4929件 (Win 1502 / Loss 1623 / Flat 1804) / skip 4926件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $832.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$175.81** / 初期 $100.00 (+75.81%)
- 確定: 2273件 (Win 635 / Loss 545 / Flat 1093) / skip 4432件
- 成長率目線: 平均log +0.000248 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0917 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $175.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.88** / 初期 $100.00 (+14.88%)
- 確定: 2089件 (Win 610 / Loss 817 / Flat 662) / pending 0件 / skip 2678件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000298 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FILECOIN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.88

## 6. Latest Market Context

- 更新: 2026-09-02T03:16:15.788905+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.26% price=77499.9
- Funnel: target 1036 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UAI/USDT:USDT | +30.55% | $18,370,192.76 |
| MAGMA/USDT:USDT | +27.51% | $5,262,741.03 |
| CASHCAT/USDT:USDT | +26.02% | $1,394,964.28 |
| HEMI/USDT:USDT | +13.75% | $6,443,348.82 |
| FILECOIN/USDT:USDT | +10.91% | $22,652,348.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MARSCOIN/USDT:USDT | below_1h_threshold | +4.34% | +4.08% |
| UAI/USDT:USDT | below_1h_threshold | +2.64% | +2.39% |
| SKR/USDT:USDT | below_1h_threshold | +2.63% | +2.37% |
| NIULAI/USDT:USDT | below_1h_threshold | +2.62% | +2.36% |
| ZORA/USDT:USDT | below_1h_threshold | +1.77% | +1.51% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
