# Decision Report

- generated_at: 2026-06-22T14:23:32.532292+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7373**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.18% / filled 20/20。**
- 全期間 MARKET基準: n=7373, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.18% | **+1.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.24% | **+1.24%** |
| MARKET | 20/20 | 100.0% | +1.18% | **+1.18%** |
| LIMIT_BB3S | 6/17 | 35.3% | +2.60% | **+0.92%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.09% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |
| MARKET_LONG | 20/20 | 100.0% | +0.12% | **+0.12%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.12% | **+0.04%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | -0.20% | **-0.13%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | -0.29% | **-0.19%** |

## 2. $100 Live Portfolio

- 残高: **$102.45** / 初期 $100.00 (+2.45%)
- 確定トレード: 28件 (TP 11 / SL 17 / EXP 0)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.45
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$230.59** / 初期 $100.00 (+130.59%)
- 確定: 2034件 (Win 600 / Loss 669 / Flat 765) / skip 1900件
- 成長率目線: 平均log +0.000411 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $230.59

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 312件 (Win 89 / Loss 87 / Flat 136) / skip 472件
- 成長率目線: 平均log +0.000188 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-22T14:23:29.409897+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.73% price=65068.7
- Funnel: target 808 → liquid 155 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +63.16% | $20,760,117.67 |
| BEL/USDT:USDT | +36.45% | $2,495,872.47 |
| BTW/USDT:USDT | +32.34% | $35,535,022.82 |
| CLO/USDT:USDT | +24.63% | $3,316,570.85 |
| BLESS/USDT:USDT | +22.32% | $2,271,365.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +3.74% | +4.47% |
| CLO/USDT:USDT | below_1h_threshold | +2.35% | +3.08% |
| BTW/USDT:USDT | below_1h_threshold | +1.70% | +2.43% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +1.11% | +1.84% |
| LAYER/USDT:USDT | below_1h_threshold | +1.01% | +1.74% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
