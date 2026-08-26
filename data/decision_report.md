# Decision Report

- generated_at: 2026-08-26T13:16:23.133851+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12708**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.24% / filled 20/20。**
- 全期間 MARKET基準: n=12708, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.24% | **+2.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.24% | **+2.24%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.77% | **+1.59%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.67% | **+1.17%** |
| LIMIT_BB3S | 10/16 | 62.5% | +1.78% | **+1.11%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.33% | **+0.93%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +1.24% | **+0.56%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -0.24% | **-0.12%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | -0.43% | **-0.24%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$690.03** / 初期 $100.00 (+590.03%)
- 確定: 4607件 (Win 1400 / Loss 1516 / Flat 1691) / skip 4662件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONG/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $690.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2001件 (Win 544 / Loss 483 / Flat 974) / skip 4118件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0600 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.00** / 初期 $100.00 (+16.00%)
- 確定: 1980件 (Win 580 / Loss 756 / Flat 644) / pending 2件 / skip 2196件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000266 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONG/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.00

## 6. Latest Market Context

- 更新: 2026-08-26T13:16:10.112599+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=78110.0
- Funnel: target 1023 → liquid 162 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +265.50% | $19,544,805.96 |
| TAC/USDT:USDT | +50.11% | $8,020,536.65 |
| BMT/USDT:USDT | +48.79% | $16,203,460.23 |
| LONGXIA/USDT:USDT | +35.87% | $1,997,928.79 |
| LIGHT/USDT:USDT | +17.06% | $1,587,031.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| METASTOCK/USDT:USDT | below_1h_threshold | +2.27% | +2.49% |
| SOXS/USDT:USDT | below_1h_threshold | +1.91% | +2.12% |
| TAC/USDT:USDT | below_1h_threshold | +1.70% | +1.92% |
| EDEN/USDT:USDT | below_1h_threshold | +1.31% | +1.52% |
| TUT/USDT:USDT | below_1h_threshold | +0.85% | +1.07% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
