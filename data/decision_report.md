# Decision Report

- generated_at: 2026-08-15T02:21:19.240603+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11627**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11627, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.05% | **+0.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.31% | **+0.66%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.05% | **+1.05%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.70% | **+0.56%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +0.55% | **+0.55%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$642.60** / 初期 $100.00 (+542.60%)
- 確定: 4095件 (Win 1284 / Loss 1349 / Flat 1462) / skip 4093件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $642.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$152.49** / 初期 $100.00 (+52.49%)
- 確定: 1690件 (Win 483 / Loss 409 / Flat 798) / skip 3348件
- 成長率目線: 平均log +0.000250 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0553 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $152.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.51** / 初期 $100.00 (+17.51%)
- 確定: 1574件 (Win 479 / Loss 603 / Flat 492) / pending 1件 / skip 1522件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000154 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AIO/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $117.51

## 6. Latest Market Context

- 更新: 2026-08-15T02:21:11.227842+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=63055.5
- Funnel: target 985 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROBO/USDT:USDT | +26.66% | $1,727,468.16 |
| CAP/USDT:USDT | +17.08% | $21,806,236.42 |
| US/USDT:USDT | +14.67% | $6,675,020.94 |
| CYS/USDT:USDT | +13.82% | $16,192,653.73 |
| AIO/USDT:USDT | +13.03% | $1,253,020.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ROBO/USDT:USDT | below_1h_threshold | +4.04% | +3.97% |
| CAP/USDT:USDT | below_1h_threshold | +3.76% | +3.69% |
| LINK/USDT:USDT | below_1h_threshold | +2.58% | +2.51% |
| BTW/USDT:USDT | below_1h_threshold | +1.79% | +1.72% |
| VELVET/USDT:USDT | below_1h_threshold | +1.70% | +1.63% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
