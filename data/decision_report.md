# Decision Report

- generated_at: 2026-06-17T21:38:58.893248+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6969**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.34% / filled 20/20。**
- 全期間 MARKET基準: n=6969, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.40% | **+0.40%** |
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.58% | **+0.17%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.20% | **+0.16%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.19% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +4.81% | **+2.89%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.33% | **+1.06%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.28% | **+0.83%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.00% | **+0.75%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$198.71** / 初期 $100.00 (+98.71%)
- 確定: 1818件 (Win 496 / Loss 573 / Flat 749) / skip 1712件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $198.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$103.26** / 初期 $100.00 (+3.26%)
- 確定: 242件 (Win 64 / Loss 60 / Flat 118) / skip 138件
- 成長率目線: 平均log +0.000133 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0691 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $103.26

## 5. Latest Market Context

- 更新: 2026-06-17T21:38:54.741096+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=64348.7
- Funnel: target 790 → liquid 172 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| O/USDT:USDT | +92.44% | $1,181,848.41 |
| SYN/USDT:USDT | +53.69% | $3,156,413.78 |
| RE/USDT:USDT | +14.10% | $1,734,497.93 |
| MITO/USDT:USDT | +10.11% | $1,544,166.75 |
| TAC/USDT:USDT | +9.80% | $2,561,779.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FOLKS/USDT:USDT | below_1h_threshold | +3.55% | +3.64% |
| EVAA/USDT:USDT | below_1h_threshold | +3.09% | +3.18% |
| ALLO/USDT:USDT | below_1h_threshold | +2.49% | +2.58% |
| TAC/USDT:USDT | below_1h_threshold | +2.03% | +2.12% |
| MITO/USDT:USDT | below_1h_threshold | +1.76% | +1.85% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
