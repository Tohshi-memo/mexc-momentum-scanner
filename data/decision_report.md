# Decision Report

- generated_at: 2026-07-22T14:37:06.581462+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9287**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.31% / filled 20/20。**
- 全期間 MARKET基準: n=9287, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_BB3S | 3/16 | 18.8% | +1.88% | **+0.35%** |
| MARKET | 20/20 | 100.0% | +0.31% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +2.16% | **+2.16%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.86% | **+0.78%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.59% | **+0.24%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +0.87% | **+0.22%** |
| MARKET_LONG | 20/20 | 100.0% | +0.10% | **+0.10%** |

## 2. $100 Live Portfolio

- 残高: **$104.85** / 初期 $100.00 (+4.85%)
- 確定トレード: 131件 (TP 44 / SL 82 / EXP 5)
- 最新: NIGHT/USDT:USDT SL_HIT PnL -4.00% 残高後 $104.85
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$432.89** / 初期 $100.00 (+332.89%)
- 確定: 3284件 (Win 1037 / Loss 1055 / Flat 1192) / skip 2564件
- 成長率目線: 平均log +0.000446 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DELLSTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $432.89

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.82** / 初期 $100.00 (+30.82%)
- 確定: 1160件 (Win 312 / Loss 253 / Flat 595) / skip 1538件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1113 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LAB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $130.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$102.08** / 初期 $100.00 (+2.08%)
- 確定: 422件 (Win 142 / Loss 173 / Flat 107) / pending 6件 / skip 343件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000207 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $102.08

## 6. Latest Market Context

- 更新: 2026-07-22T14:36:48.377083+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.37% price=65676.4
- Funnel: target 890 → liquid 180 → pre 50 → checked 50 → surge 12 → strict 5
- Surge前reject: below_1h_threshold=38, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.3 >= 65=1, 4h RSI 78.8 >= 65=1, 4h RSI 65.5 >= 65=1, 4h RSI 74.3 >= 65=1, 4h RSI 73.0 >= 65=1, 4h RSI 74.9 >= 65=1, 4h RSI 69.2 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RE/USDT:USDT | +30.28% | $14,831,857.41 |
| SMCISTOCK/USDT:USDT | +24.15% | $5,691,275.68 |
| BLESS/USDT:USDT | +23.59% | $2,243,853.64 |
| JIMOTHY/USDT:USDT | +18.84% | $3,480,028.20 |
| LAB/USDT:USDT | +18.10% | $14,990,425.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| INTCSTOCK/USDT:USDT | below_1h_threshold | +4.76% | +5.14% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +4.63% | +5.00% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +4.52% | +4.89% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +3.91% | +4.28% |
| TLM/USDT:USDT | below_1h_threshold | +2.23% | +2.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
