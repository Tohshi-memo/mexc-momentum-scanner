# Decision Report

- generated_at: 2026-07-01T15:06:09.950581+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7996**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7996, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-1.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.83% | **-1.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.91% | **+0.69%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.47% | **+0.65%** |
| LIMIT_8PCT | 2/20 | 10.0% | +6.03% | **+0.60%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.01% | **+0.30%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.40% | **-0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +3.46% | **+1.73%** |
| MARKET_LONG | 20/20 | 100.0% | +1.41% | **+1.41%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.86% | **+1.29%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.60% | **+1.04%** |
| ASK_LONG | 20/20 | 100.0% | +1.02% | **+1.02%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$266.72** / 初期 $100.00 (+166.72%)
- 確定: 2394件 (Win 728 / Loss 792 / Flat 874) / skip 2163件
- 成長率目線: 平均log +0.000410 / 幾何平均 +0.041% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NES/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $266.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.42** / 初期 $100.00 (+6.42%)
- 確定: 515件 (Win 129 / Loss 123 / Flat 263) / skip 892件
- 成長率目線: 平均log +0.000121 / 幾何平均 +0.012% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0309 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NES/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.42

## 5. Latest Market Context

- 更新: 2026-07-01T15:06:04.055864+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.54% price=59840.3
- Funnel: target 825 → liquid 149 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAIKO/USDT:USDT | +77.28% | $16,857,661.29 |
| M/USDT:USDT | +62.34% | $7,074,802.26 |
| ZBT/USDT:USDT | +27.64% | $3,249,273.10 |
| BASED/USDT:USDT | +24.97% | $14,736,983.77 |
| NES/USDT:USDT | +23.75% | $1,256,002.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NES/USDT:USDT | below_1h_threshold | +2.21% | +1.67% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +1.81% | +1.27% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.16% | +0.63% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +0.78% | +0.25% |
| METASTOCK/USDT:USDT | below_1h_threshold | +0.75% | +0.21% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
