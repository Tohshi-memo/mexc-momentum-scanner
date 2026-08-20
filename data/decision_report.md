# Decision Report

- generated_at: 2026-08-20T08:46:25.247285+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12022**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12022, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.00% | **-0.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_BB3S | 7/14 | 50.0% | +0.81% | **+0.41%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.02% | **+0.01%** |
| LIMIT_8PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.39% | **+0.77%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.07% | **+0.48%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.62% | **+0.43%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.71% | **+0.42%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.63% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$600.15** / 初期 $100.00 (+500.15%)
- 確定: 4246件 (Win 1303 / Loss 1390 / Flat 1553) / skip 4337件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.50% 残高後 $600.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.70** / 初期 $100.00 (+54.70%)
- 確定: 1821件 (Win 502 / Loss 428 / Flat 891) / skip 3612件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $154.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.76** / 初期 $100.00 (+16.76%)
- 確定: 1754件 (Win 520 / Loss 670 / Flat 564) / pending 3件 / skip 1739件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000431 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MINIMAXSTOCK/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.76

## 6. Latest Market Context

- 更新: 2026-08-20T08:46:16.420701+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +2.37% price=71473.4
- Funnel: target 1004 → liquid 200 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BOME/USDT:USDT | +35.01% | $4,872,986.32 |
| NIULAI/USDT:USDT | +33.07% | $2,184,098.31 |
| MAGMA/USDT:USDT | +28.83% | $7,794,633.14 |
| MET/USDT:USDT | +22.27% | $1,008,190.08 |
| RED/USDT:USDT | +21.07% | $2,173,686.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PEPE/USDT:USDT | below_relative_strength | +6.15% | +3.77% |
| USELESS/USDT:USDT | below_1h_threshold | +4.31% | +1.94% |
| ON/USDT:USDT | below_1h_threshold | +3.71% | +1.34% |
| SHIB/USDT:USDT | below_1h_threshold | +3.68% | +1.30% |
| XRP/USDT:USDT | below_1h_threshold | +3.44% | +1.07% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
