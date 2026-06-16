# Decision Report

- generated_at: 2026-06-16T06:25:50.520830+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6843**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6843, expectancy=-0.05%
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
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.09% | **+0.55%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.38% | **+0.15%** |
| LIMIT_3PCT | 17/20 | 85.0% | -0.04% | **-0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +4.57% | **+1.60%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.00% | **+1.05%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +2.98% | **+1.04%** |
| MARKET_LONG | 20/20 | 100.0% | +0.98% | **+0.98%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +1.96% | **+0.78%** |

## 2. $100 Live Portfolio

- 残高: **$102.50** / 初期 $100.00 (+2.50%)
- 確定トレード: 10件 (TP 5 / SL 5 / EXP 0)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.50
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$182.43** / 初期 $100.00 (+82.43%)
- 確定: 1716件 (Win 447 / Loss 535 / Flat 734) / skip 1688件
- 成長率目線: 平均log +0.000350 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SPACE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $182.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 156件 (Win 28 / Loss 30 / Flat 98) / skip 98件
- 成長率目線: 平均log -0.000155 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0541 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-16T06:25:45.227546+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.29% price=66224.2
- Funnel: target 777 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +58.62% | $3,601,621.22 |
| VELVET/USDT:USDT | +35.29% | $12,919,879.24 |
| SPACE/USDT:USDT | +32.67% | $2,542,626.47 |
| BSB/USDT:USDT | +26.88% | $21,539,478.78 |
| ASTEROID/USDT:USDT | +25.45% | $5,418,590.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPACE/USDT:USDT | below_1h_threshold | +4.13% | +3.84% |
| RIF/USDT:USDT | below_1h_threshold | +3.20% | +2.90% |
| FOLKS/USDT:USDT | below_1h_threshold | +1.78% | +1.48% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +1.25% | +0.95% |
| WLD/USDT:USDT | below_1h_threshold | +1.18% | +0.89% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
