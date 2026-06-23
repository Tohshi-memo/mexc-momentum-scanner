# Decision Report

- generated_at: 2026-06-23T19:22:52.844062+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7438**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.17% / filled 20/20。**
- 全期間 MARKET基準: n=7438, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+1.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |
| ASK | 20/20 | 100.0% | +1.13% | **+1.13%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.82% | **+0.38%** |
| LIMIT_BB3S | 5/14 | 35.7% | +0.47% | **+0.17%** |
| LIMIT_1PCT | 15/20 | 75.0% | +0.07% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +3.19% | **+0.48%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.20% | **+0.18%** |

## 2. $100 Live Portfolio

- 残高: **$101.43** / 初期 $100.00 (+1.43%)
- 確定トレード: 30件 (TP 11 / SL 19 / EXP 0)
- 最新: HEI/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.43
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$228.71** / 初期 $100.00 (+128.71%)
- 確定: 2081件 (Win 617 / Loss 690 / Flat 774) / skip 1918件
- 成長率目線: 平均log +0.000398 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $228.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.36** / 初期 $100.00 (+6.36%)
- 確定: 324件 (Win 92 / Loss 88 / Flat 144) / skip 525件
- 成長率目線: 平均log +0.000190 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_robust_growth_score) / robust_score -0.0375 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $106.36

## 5. Latest Market Context

- 更新: 2026-06-23T19:22:45.699647+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=62259.4
- Funnel: target 802 → liquid 168 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +49.26% | $3,440,877.65 |
| BEAT/USDT:USDT | +14.78% | $24,563,320.90 |
| SYN/USDT:USDT | +9.43% | $17,588,368.38 |
| BASED/USDT:USDT | +5.91% | $2,828,732.47 |
| ESPORTS/USDT:USDT | +5.37% | $6,983,203.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEI/USDT:USDT | below_1h_threshold | +4.94% | +4.87% |
| AMCSTOCK/USDT:USDT | below_1h_threshold | +3.51% | +3.43% |
| GRASS/USDT:USDT | below_1h_threshold | +2.06% | +1.98% |
| CCLSTOCK/USDT:USDT | below_1h_threshold | +1.86% | +1.79% |
| SAHARA/USDT:USDT | below_1h_threshold | +1.76% | +1.69% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
