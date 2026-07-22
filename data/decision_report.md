# Decision Report

- generated_at: 2026-07-22T15:56:27.303217+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9292**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.77% / filled 20/20。**
- 全期間 MARKET基準: n=9292, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.19% | **+1.07%** |
| LIMIT_3PCT | 12/20 | 60.0% | +1.40% | **+0.84%** |
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.91% | **+0.63%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.66% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +0.93% | **+0.93%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +0.60% | **+0.18%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.00% | **+0.00%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.14% | **-0.01%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.11% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$105.90** / 初期 $100.00 (+5.90%)
- 確定トレード: 132件 (TP 45 / SL 82 / EXP 5)
- 最新: PROM/USDT:USDT TP_HIT PnL +8.00% 残高後 $105.90
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$429.20** / 初期 $100.00 (+329.20%)
- 確定: 3288件 (Win 1038 / Loss 1058 / Flat 1192) / skip 2565件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $429.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.82** / 初期 $100.00 (+30.82%)
- 確定: 1160件 (Win 312 / Loss 253 / Flat 595) / skip 1543件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0617 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $130.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.55** / 初期 $100.00 (+1.55%)
- 確定: 425件 (Win 142 / Loss 176 / Flat 107) / pending 3件 / skip 346件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000130 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $101.55

## 6. Latest Market Context

- 更新: 2026-07-22T15:56:21.758816+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.37% price=66015.6
- Funnel: target 890 → liquid 183 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.8 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RE/USDT:USDT | +26.39% | $16,511,276.14 |
| SMCISTOCK/USDT:USDT | +26.02% | $6,256,915.11 |
| MIRA/USDT:USDT | +24.14% | $1,522,320.32 |
| JIMOTHY/USDT:USDT | +20.49% | $3,551,787.12 |
| LAB/USDT:USDT | +19.35% | $15,453,544.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +3.34% | +2.97% |
| LAB/USDT:USDT | below_1h_threshold | +3.12% | +2.74% |
| INFQSTOCK/USDT:USDT | below_1h_threshold | +2.81% | +2.44% |
| LIT/USDT:USDT | below_1h_threshold | +1.96% | +1.59% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +1.84% | +1.47% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
