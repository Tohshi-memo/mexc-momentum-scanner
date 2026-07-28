# Decision Report

- generated_at: 2026-07-28T15:31:33.421267+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9704**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9704, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.91%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.91% | **-0.91%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.16% | **+0.29%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.52% | **+0.29%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_BB3S | 4/19 | 21.1% | +0.53% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +3.25% | **+2.44%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.69% | **+1.53%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.92% | **+0.96%** |
| MARKET_LONG | 20/20 | 100.0% | +0.91% | **+0.91%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +2.53% | **+0.89%** |

## 2. $100 Live Portfolio

- 残高: **$106.38** / 初期 $100.00 (+6.38%)
- 確定トレード: 149件 (TP 51 / SL 93 / EXP 5)
- 最新: BANK/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.38
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$477.29** / 初期 $100.00 (+377.29%)
- 確定: 3474件 (Win 1096 / Loss 1126 / Flat 1252) / skip 2791件
- 成長率目線: 平均log +0.000450 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ON/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $477.29

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1226件 (Win 338 / Loss 275 / Flat 613) / skip 1889件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1038 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SPCXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$109.39** / 初期 $100.00 (+9.39%)
- 確定: 722件 (Win 235 / Loss 275 / Flat 212) / pending 6件 / skip 449件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000386 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SPCXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $109.39

## 6. Latest Market Context

- 更新: 2026-07-28T15:31:26.785066+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.55% price=63733.5
- Funnel: target 904 → liquid 176 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.8 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COTI/USDT:USDT | +54.50% | $23,562,054.29 |
| ON/USDT:USDT | +44.61% | $21,835,302.03 |
| SOONNETWORK/USDT:USDT | +35.28% | $3,023,098.77 |
| BULLA/USDT:USDT | +26.49% | $2,201,080.04 |
| VANRY/USDT:USDT | +23.23% | $1,533,517.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SPCXSTOCK/USDT:USDT | below_relative_strength | +5.47% | +4.92% |
| XPL/USDT:USDT | below_1h_threshold | +3.14% | +2.59% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +3.06% | +2.51% |
| JUP/USDT:USDT | below_1h_threshold | +2.69% | +2.14% |
| VANRY/USDT:USDT | below_1h_threshold | +2.61% | +2.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
