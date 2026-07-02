# Decision Report

- generated_at: 2026-07-02T10:12:21.495254+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8060**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +4.40% / filled 20/20。**
- 全期間 MARKET基準: n=8060, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+4.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.40% | **+4.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +4.40% | **+4.40%** |
| ASK | 20/20 | 100.0% | +4.39% | **+4.39%** |
| LIMIT_1PCT | 11/20 | 55.0% | +1.55% | **+0.85%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.54% | **+0.31%** |
| LIMIT_2PCT | 9/20 | 45.0% | +0.68% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +2.15% | **+0.64%** |
| LIMIT_9PCT_LONG | 11/20 | 55.0% | +0.34% | **+0.18%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -0.46% | **-0.12%** |
| LIMIT_8PCT_LONG | 14/20 | 70.0% | -0.29% | **-0.20%** |
| LIMIT_7PCT_LONG | 15/20 | 75.0% | -1.06% | **-0.79%** |

## 2. $100 Live Portfolio

- 残高: **$103.14** / 初期 $100.00 (+3.14%)
- 確定トレード: 49件 (TP 18 / SL 30 / EXP 1)
- 最新: NOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.67** / 初期 $100.00 (+184.67%)
- 確定: 2444件 (Win 754 / Loss 816 / Flat 874) / skip 2177件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $284.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.14** / 初期 $100.00 (+5.14%)
- 確定: 550件 (Win 136 / Loss 131 / Flat 283) / skip 921件
- 成長率目線: 平均log +0.000091 / 幾何平均 +0.009% per trade / maxDD +3.53%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0419 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BIRB/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $105.14

## 5. Latest Market Context

- 更新: 2026-07-02T10:12:13.127268+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=61108.4
- Funnel: target 834 → liquid 165 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BIRB/USDT:USDT | +60.30% | $6,250,509.19 |
| BREV/USDT:USDT | +43.70% | $3,685,586.37 |
| SYN/USDT:USDT | +25.59% | $19,282,496.40 |
| TLM/USDT:USDT | +25.35% | $8,977,112.03 |
| M/USDT:USDT | +21.73% | $7,529,156.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NOM/USDT:USDT | below_1h_threshold | +3.45% | +3.53% |
| USELESS/USDT:USDT | below_1h_threshold | +2.00% | +2.09% |
| GRAM/USDT:USDT | below_1h_threshold | +1.35% | +1.43% |
| BREV/USDT:USDT | below_1h_threshold | +1.34% | +1.43% |
| FILECOIN/USDT:USDT | below_1h_threshold | +1.30% | +1.38% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
