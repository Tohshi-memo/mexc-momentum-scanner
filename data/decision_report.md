# Decision Report

- generated_at: 2026-11-06T06:36:30.334612+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18257**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18257, expectancy=+0.03%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 12/20 | 60.0% | +1.71% | **+1.03%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.92% | **+0.77%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.76% | **+0.34%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.38% | **+2.02%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.88% | **+1.22%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 264件 (TP 97 / SL 159 / EXP 8)
- 最新: CSOPSKHYNIX2L/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,477.20** / 初期 $100.00 (+1377.20%)
- 確定: 7035件 (Win 2022 / Loss 2247 / Flat 2766) / skip 7783件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,477.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$373.03** / 初期 $100.00 (+273.03%)
- 確定: 4627件 (Win 1243 / Loss 1034 / Flat 2350) / skip 7041件
- 成長率目線: 平均log +0.000285 / 幾何平均 +0.028% per trade / maxDD +4.29%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.1146 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LYN/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $373.03

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6417件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000224 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-06T06:36:14.740775+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=75618.8
- Funnel: target 1084 → liquid 186 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +79.65% | $28,555,261.83 |
| UAI/USDT:USDT | +53.77% | $9,631,280.60 |
| CYBER/USDT:USDT | +44.77% | $3,110,111.07 |
| LYN/USDT:USDT | +21.10% | $1,501,215.46 |
| IRENSTOCK/USDT:USDT | +17.45% | $3,135,435.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +3.03% | +3.10% |
| LAB/USDT:USDT | below_1h_threshold | +1.52% | +1.59% |
| PEPE/USDT:USDT | below_1h_threshold | +1.52% | +1.58% |
| UVXY/USDT:USDT | below_1h_threshold | +1.43% | +1.50% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +1.43% | +1.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
