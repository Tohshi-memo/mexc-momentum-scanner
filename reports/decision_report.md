# Decision Report

- generated_at: 2026-06-13T15:22:31.929605+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6586**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6586, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.76% | **-1.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.08% | **+0.07%** |
| LIMIT_ATR | 18/20 | 90.0% | +0.03% | **+0.02%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.12% | **-0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.25% | **+1.25%** |
| MARKET_LONG | 20/20 | 100.0% | +1.21% | **+1.21%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +2.09% | **+1.05%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +1.30% | **+0.78%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +1.73% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$164.87** / 初期 $100.00 (+64.87%)
- 確定: 1459件 (Win 391 / Loss 464 / Flat 604) / skip 1688件
- 成長率目線: 平均log +0.000343 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COAI/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $164.87

## 4. Robust Adaptive DryRun ($100)

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定: 0件 (Win 0 / Loss 0 / Flat 0) / skip 0件
- 成長率目線: 平均log +0.000000 / 幾何平均 +0.000% per trade / maxDD +0.00%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0167 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 状態: 新しい$100口座として開始済み。開始後に閉じたシャドウトレードから反映します。

## 5. Latest Market Context

- 更新: 2026-06-13T15:22:27.604358+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=64283.3
- Funnel: target 770 → liquid 142 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COAI/USDT:USDT | +62.63% | $11,724,090.24 |
| JCT/USDT:USDT | +45.04% | $9,687,804.17 |
| RIF/USDT:USDT | +35.28% | $5,444,625.47 |
| TAO/USDT:USDT | +25.48% | $200,436,980.12 |
| EDGE/USDT:USDT | +16.53% | $3,429,185.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +4.04% | +3.89% |
| TIA/USDT:USDT | below_1h_threshold | +3.85% | +3.70% |
| NEAR/USDT:USDT | below_1h_threshold | +2.41% | +2.26% |
| BTW/USDT:USDT | below_1h_threshold | +2.38% | +2.23% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.36% | +2.21% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
