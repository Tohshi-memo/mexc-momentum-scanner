# Decision Report

- generated_at: 2026-06-29T11:58:06.659486+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7813**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7813, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +2.68% | **+1.07%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.54% | **+0.76%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.02% | **+0.76%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.33% | **+0.33%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.40% | **+1.32%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +4.29% | **+1.07%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_BB3S_LONG | 5/11 | 45.5% | +1.86% | **+0.85%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.29% | **+0.84%** |

## 2. $100 Live Portfolio

- 残高: **$102.14** / 初期 $100.00 (+2.14%)
- 確定トレード: 42件 (TP 15 / SL 26 / EXP 1)
- 最新: G/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$264.58** / 初期 $100.00 (+164.58%)
- 確定: 2317件 (Win 706 / Loss 772 / Flat 839) / skip 2057件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RE/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $264.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 456件 (Win 120 / Loss 119 / Flat 217) / skip 768件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0341 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-29T11:58:01.464336+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.32% price=59870.0
- Funnel: target 810 → liquid 143 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.0 >= 65=1, 4h RSI 72.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAC/USDT:USDT | +140.55% | $21,442,462.38 |
| GWEI/USDT:USDT | +46.91% | $1,774,236.41 |
| RAVE/USDT:USDT | +28.48% | $43,082,559.45 |
| UB/USDT:USDT | +28.14% | $2,104,824.97 |
| G/USDT:USDT | +26.03% | $2,402,969.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +4.30% | +4.62% |
| GWEI/USDT:USDT | below_1h_threshold | +3.86% | +4.18% |
| SLX/USDT:USDT | below_1h_threshold | +3.32% | +3.64% |
| ANSEM/USDT:USDT | below_1h_threshold | +2.80% | +3.12% |
| BEAT/USDT:USDT | below_1h_threshold | +2.55% | +2.87% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
