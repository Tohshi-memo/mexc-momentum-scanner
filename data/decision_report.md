# Decision Report

- generated_at: 2026-06-13T15:41:23.869975+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6587**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6587, expectancy=-0.06%
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
| LIMIT_4PCT | 16/20 | 80.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.12% | **-0.04%** |
| LIMIT_ATR | 18/20 | 90.0% | -0.05% | **-0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +2.09% | **+1.05%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.37% | **+0.95%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.09% | **+0.94%** |
| ASK_LONG | 20/20 | 100.0% | +0.84% | **+0.84%** |
| MARKET_LONG | 20/20 | 100.0% | +0.81% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$164.87** / 初期 $100.00 (+64.87%)
- 確定: 1460件 (Win 391 / Loss 464 / Flat 605) / skip 1688件
- 成長率目線: 平均log +0.000342 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RIF/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $164.87

## 4. Robust Adaptive DryRun ($100)

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定: 0件 (Win 0 / Loss 0 / Flat 0) / skip 0件
- 成長率目線: 平均log +0.000000 / 幾何平均 +0.000% per trade / maxDD +0.00%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0167 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 状態: 新しい$100口座として開始済み。開始後に閉じたシャドウトレードから反映します。

## 5. Latest Market Context

- 更新: 2026-06-13T15:41:19.019041+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=64289.2
- Funnel: target 770 → liquid 143 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.5 >= 65=2
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COAI/USDT:USDT | +67.41% | $13,122,043.31 |
| JCT/USDT:USDT | +42.92% | $9,732,793.35 |
| RIF/USDT:USDT | +39.13% | $5,628,740.06 |
| TAO/USDT:USDT | +24.07% | $206,162,213.75 |
| MEGA/USDT:USDT | +16.42% | $1,382,250.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MEGA/USDT:USDT | below_1h_threshold | +4.34% | +4.18% |
| TIA/USDT:USDT | below_1h_threshold | +3.73% | +3.57% |
| BTW/USDT:USDT | below_1h_threshold | +3.01% | +2.84% |
| NEAR/USDT:USDT | below_1h_threshold | +2.66% | +2.49% |
| ICP/USDT:USDT | below_1h_threshold | +2.04% | +1.88% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
