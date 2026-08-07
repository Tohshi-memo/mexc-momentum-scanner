# Decision Report

- generated_at: 2026-08-07T21:21:33.234354+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10760**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10760, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.47% | **-1.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +6.62% | **+1.66%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.47% | **+0.42%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_BB3S | 3/16 | 18.8% | +1.09% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.08% | **+1.77%** |
| MARKET_LONG | 20/20 | 100.0% | +1.47% | **+1.47%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +3.14% | **+1.41%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +2.94% | **+0.88%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.37% | **+0.82%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$595.60** / 初期 $100.00 (+495.60%)
- 確定: 3800件 (Win 1203 / Loss 1250 / Flat 1347) / skip 3521件
- 成長率目線: 平均log +0.000470 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $595.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.91** / 初期 $100.00 (+43.91%)
- 確定: 1480件 (Win 416 / Loss 347 / Flat 717) / skip 2691件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $143.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.43** / 初期 $100.00 (+18.43%)
- 確定: 1180件 (Win 381 / Loss 466 / Flat 333) / pending 2件 / skip 1053件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000085 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEI/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $118.43

## 6. Latest Market Context

- 更新: 2026-08-07T21:21:19.807467+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=64950.4
- Funnel: target 961 → liquid 183 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +96.16% | $2,308,121.92 |
| BLESS/USDT:USDT | +35.76% | $70,660,425.31 |
| EPIC/USDT:USDT | +15.17% | $2,133,587.96 |
| HEI/USDT:USDT | +10.95% | $20,186,591.01 |
| GWEI/USDT:USDT | +10.26% | $1,477,399.57 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEI/USDT:USDT | below_1h_threshold | +3.84% | +3.83% |
| CYS/USDT:USDT | below_1h_threshold | +2.05% | +2.04% |
| ACE/USDT:USDT | below_1h_threshold | +1.89% | +1.88% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.64% | +1.63% |
| GRVT/USDT:USDT | below_1h_threshold | +1.45% | +1.43% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
