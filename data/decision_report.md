# Decision Report

- generated_at: 2026-06-17T02:24:31.783475+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6896**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6896, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.18% | **-1.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.11% | **+0.50%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.00% | **+0.00%** |
| LIMIT_3PCT | 17/20 | 85.0% | -0.09% | **-0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.24% | **+1.57%** |
| ASK_LONG | 20/20 | 100.0% | +1.33% | **+1.33%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.85% | **+0.85%** |
| LIMIT_2PCT_LONG | 9/20 | 45.0% | +0.71% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$192.98** / 初期 $100.00 (+92.98%)
- 確定: 1769件 (Win 473 / Loss 553 / Flat 743) / skip 1688件
- 成長率目線: 平均log +0.000372 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $192.98

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.34** / 初期 $100.00 (-0.66%)
- 確定: 169件 (Win 34 / Loss 31 / Flat 104) / skip 138件
- 成長率目線: 平均log -0.000039 / 幾何平均 -0.004% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0742 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $99.34

## 5. Latest Market Context

- 更新: 2026-06-17T02:24:28.455679+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=66066.2
- Funnel: target 782 → liquid 155 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +36.30% | $7,081,711.81 |
| H/USDT:USDT | +28.59% | $56,494,345.65 |
| SQD/USDT:USDT | +19.60% | $1,334,819.26 |
| ESPORTS/USDT:USDT | +18.00% | $3,368,203.33 |
| UNI/USDT:USDT | +17.97% | $42,635,402.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +4.43% | +4.18% |
| EPIC/USDT:USDT | below_1h_threshold | +2.72% | +2.47% |
| UNI/USDT:USDT | below_1h_threshold | +2.59% | +2.34% |
| UAI/USDT:USDT | below_1h_threshold | +2.16% | +1.91% |
| VVV/USDT:USDT | below_1h_threshold | +1.69% | +1.44% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
