# Decision Report

- generated_at: 2026-10-23T06:46:26.057471+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17196**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17196, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.22% | **-0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.46% | **+0.44%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.15% | **-0.07%** |
| LIMIT_4PCT | 11/20 | 55.0% | -0.24% | **-0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +3.15% | **+1.42%** |
| MARKET_LONG | 20/20 | 100.0% | +0.32% | **+0.32%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.08% | **+0.06%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.07% | **+0.03%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,317.31** / 初期 $100.00 (+1217.31%)
- 確定: 6552件 (Win 1902 / Loss 2093 / Flat 2557) / skip 7205件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,317.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$276.15** / 初期 $100.00 (+176.15%)
- 確定: 3872件 (Win 1057 / Loss 901 / Flat 1914) / skip 6735件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +4.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0305 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $276.15

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5358件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000226 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-23T06:46:13.664089+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=81845.6
- Funnel: target 1096 → liquid 175 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +43.36% | $13,796,851.35 |
| IRYS/USDT:USDT | +28.21% | $3,840,698.00 |
| UNITREE/USDT:USDT | +20.35% | $2,055,480.97 |
| DNA/USDT:USDT | +17.99% | $4,271,924.01 |
| ZHIPUSTOCK/USDT:USDT | +10.85% | $1,897,509.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +2.38% | +2.34% |
| NIL/USDT:USDT | below_1h_threshold | +1.97% | +1.93% |
| USELESS/USDT:USDT | below_1h_threshold | +1.71% | +1.67% |
| VVV/USDT:USDT | below_1h_threshold | +1.50% | +1.46% |
| COHRSTOCK/USDT:USDT | below_1h_threshold | +1.33% | +1.29% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
