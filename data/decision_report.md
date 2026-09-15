# Decision Report

- generated_at: 2026-09-15T17:31:28.954958+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14606**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14606, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.70% | **-0.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/18 | 33.3% | +1.09% | **+0.36%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.64% | **+0.22%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.29% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +1.54% | **+1.54%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.69% | **+0.76%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +1.97% | **+0.49%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +0.24% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,064.13** / 初期 $100.00 (+964.13%)
- 確定: 5508件 (Win 1644 / Loss 1780 / Flat 2084) / skip 5659件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIN/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $1,064.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$230.42** / 初期 $100.00 (+130.42%)
- 確定: 3046件 (Win 839 / Loss 719 / Flat 1488) / skip 4971件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.35% 残高後 $230.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.11** / 初期 $100.00 (+24.11%)
- 確定: 2909件 (Win 863 / Loss 1133 / Flat 913) / pending 0件 / skip 3174件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000136 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: POWR/USDT:USDT `MARKET` EXPIRED account +0.10% 残高後 $124.11

## 6. Latest Market Context

- 更新: 2026-09-15T17:31:18.162812+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=76527.0
- Funnel: target 1060 → liquid 158 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 97.1 >= 65=1, 4h RSI 83.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +11.74% | $3,337,734.87 |
| AIN/USDT:USDT | +8.34% | $18,387,066.63 |
| SHROOM/USDT:USDT | +6.40% | $2,402,375.72 |
| POWER/USDT:USDT | +5.70% | $14,564,680.67 |
| 4/USDT:USDT | +5.42% | $1,082,705.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LONGXIA/USDT:USDT | below_1h_threshold | +4.37% | +4.14% |
| 4/USDT:USDT | below_1h_threshold | +3.40% | +3.17% |
| REZ/USDT:USDT | below_1h_threshold | +2.53% | +2.30% |
| PONS/USDT:USDT | below_1h_threshold | +2.18% | +1.96% |
| FF/USDT:USDT | below_1h_threshold | +1.94% | +1.71% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
