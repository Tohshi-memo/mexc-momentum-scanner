# Decision Report

- generated_at: 2026-08-15T02:11:25.940373+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11626**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11626, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.04% | **-0.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 11/20 | 55.0% | +1.92% | **+1.06%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.34% | **+0.33%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.05% | **+1.05%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.70% | **+0.56%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +0.55% | **+0.55%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.44% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$645.83** / 初期 $100.00 (+545.83%)
- 確定: 4094件 (Win 1284 / Loss 1348 / Flat 1462) / skip 4093件
- 成長率目線: 平均log +0.000456 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ROBO/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $645.83

## 4. Robust Adaptive DryRun ($100)

- 残高: **$152.49** / 初期 $100.00 (+52.49%)
- 確定: 1689件 (Win 483 / Loss 409 / Flat 797) / skip 3348件
- 成長率目線: 平均log +0.000250 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0709 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ROBO/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $152.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.72** / 初期 $100.00 (+17.72%)
- 確定: 1573件 (Win 479 / Loss 602 / Flat 492) / pending 2件 / skip 1522件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000203 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ROBO/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $117.72

## 6. Latest Market Context

- 更新: 2026-08-15T02:11:15.880827+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=63021.4
- Funnel: target 985 → liquid 170 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROBO/USDT:USDT | +28.08% | $1,504,909.26 |
| AIO/USDT:USDT | +17.17% | $1,208,492.19 |
| US/USDT:USDT | +15.67% | $6,658,942.40 |
| CAP/USDT:USDT | +15.57% | $21,750,611.21 |
| CYS/USDT:USDT | +12.24% | $16,154,860.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CAP/USDT:USDT | below_1h_threshold | +2.51% | +2.50% |
| BTW/USDT:USDT | below_1h_threshold | +2.14% | +2.12% |
| LINK/USDT:USDT | below_1h_threshold | +1.78% | +1.77% |
| VELVET/USDT:USDT | below_1h_threshold | +1.66% | +1.64% |
| AEON1/USDT:USDT | below_1h_threshold | +0.87% | +0.86% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
