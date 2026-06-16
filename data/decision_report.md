# Decision Report

- generated_at: 2026-06-16T06:45:21.678659+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6846**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6846, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.55% | **-1.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.05% | **+0.42%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.38% | **+0.15%** |
| LIMIT_3PCT | 17/20 | 85.0% | -0.04% | **-0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +4.57% | **+1.60%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.00% | **+1.05%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +2.98% | **+1.04%** |
| MARKET_LONG | 20/20 | 100.0% | +0.98% | **+0.98%** |
| ASK_LONG | 20/20 | 100.0% | +0.81% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$102.50** / 初期 $100.00 (+2.50%)
- 確定トレード: 10件 (TP 5 / SL 5 / EXP 0)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.50
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$184.26** / 初期 $100.00 (+84.26%)
- 確定: 1719件 (Win 448 / Loss 535 / Flat 736) / skip 1688件
- 成長率目線: 平均log +0.000356 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $184.26

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 156件 (Win 28 / Loss 30 / Flat 98) / skip 101件
- 成長率目線: 平均log -0.000155 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0612 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-16T06:45:17.157307+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.51% price=66363.7
- Funnel: target 777 → liquid 159 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +61.63% | $3,735,490.27 |
| SPACE/USDT:USDT | +35.65% | $2,627,474.17 |
| BSB/USDT:USDT | +34.65% | $22,538,035.89 |
| VELVET/USDT:USDT | +33.96% | $14,167,167.71 |
| ASTEROID/USDT:USDT | +26.55% | $5,438,125.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +3.09% | +2.58% |
| FOLKS/USDT:USDT | below_1h_threshold | +2.66% | +2.16% |
| WLD/USDT:USDT | below_1h_threshold | +2.11% | +1.60% |
| SIREN/USDT:USDT | below_1h_threshold | +2.00% | +1.50% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +1.95% | +1.44% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
