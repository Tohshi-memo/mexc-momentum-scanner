# Decision Report

- generated_at: 2026-08-30T04:31:28.946179+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13012**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13012, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.75% | **-1.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.15% | **+0.79%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.50% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +3.70% | **+2.59%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +4.25% | **+2.55%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +4.45% | **+2.00%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.93% | **+1.76%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.10% | **+0.82%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$787.12** / 初期 $100.00 (+687.12%)
- 確定: 4782件 (Win 1459 / Loss 1575 / Flat 1748) / skip 4791件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $787.12

## 4. Robust Adaptive DryRun ($100)

- 残高: **$172.45** / 初期 $100.00 (+72.45%)
- 確定: 2096件 (Win 586 / Loss 511 / Flat 999) / skip 4327件
- 成長率目線: 平均log +0.000260 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0733 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $172.45

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.23** / 初期 $100.00 (+16.23%)
- 確定: 2056件 (Win 604 / Loss 800 / Flat 652) / pending 4件 / skip 2424件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000313 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.23

## 6. Latest Market Context

- 更新: 2026-08-30T04:31:19.399217+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=78069.7
- Funnel: target 1023 → liquid 117 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +59.70% | $2,294,595.55 |
| PONS/USDT:USDT | +49.87% | $1,490,130.62 |
| HNT/USDT:USDT | +45.81% | $28,517,620.93 |
| FONE/USDT:USDT | +43.88% | $1,310,858.54 |
| PROM/USDT:USDT | +26.43% | $14,183,232.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +4.71% | +4.76% |
| CHIP/USDT:USDT | below_1h_threshold | +3.32% | +3.37% |
| MOVR/USDT:USDT | below_1h_threshold | +3.15% | +3.20% |
| 4/USDT:USDT | below_1h_threshold | +2.35% | +2.39% |
| BTW/USDT:USDT | below_1h_threshold | +1.63% | +1.67% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
