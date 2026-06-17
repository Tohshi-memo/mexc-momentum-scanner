# Decision Report

- generated_at: 2026-06-17T20:54:55.397884+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6966**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.34% / filled 20/20。**
- 全期間 MARKET基準: n=6966, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/15 | 40.0% | +1.38% | **+0.55%** |
| ASK | 20/20 | 100.0% | +0.40% | **+0.40%** |
| MARKET | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.19% | **+0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +4.81% | **+2.89%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.56% | **+1.17%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.78% | **+0.66%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.72% | **+0.43%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$198.71** / 初期 $100.00 (+98.71%)
- 確定: 1818件 (Win 496 / Loss 573 / Flat 749) / skip 1709件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $198.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$103.28** / 初期 $100.00 (+3.28%)
- 確定: 239件 (Win 63 / Loss 58 / Flat 118) / skip 138件
- 成長率目線: 平均log +0.000135 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0607 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $103.28

## 5. Latest Market Context

- 更新: 2026-06-17T20:54:51.164783+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=64262.9
- Funnel: target 790 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| O/USDT:USDT | +74.12% | $1,127,650.69 |
| SYN/USDT:USDT | +59.08% | $2,563,718.36 |
| RE/USDT:USDT | +14.67% | $1,711,354.27 |
| MITO/USDT:USDT | +9.16% | $1,489,192.06 |
| TAC/USDT:USDT | +7.09% | $2,381,669.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +4.56% | +4.57% |
| SENT/USDT:USDT | below_1h_threshold | +3.04% | +3.06% |
| BSB/USDT:USDT | below_1h_threshold | +2.44% | +2.45% |
| WDCSTOCK/USDT:USDT | below_1h_threshold | +1.81% | +1.82% |
| ARMSTOCK/USDT:USDT | below_1h_threshold | +1.49% | +1.51% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
