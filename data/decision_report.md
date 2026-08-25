# Decision Report

- generated_at: 2026-08-25T10:21:22.622433+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12595**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=12595, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.02% | **+0.36%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.04% | **+0.02%** |
| LIMIT_1PCT | 17/20 | 85.0% | -0.04% | **-0.04%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.35% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.88% | **+0.53%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.26% | **+0.50%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.08% | **+0.43%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.06% | **+0.43%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.39% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$702.01** / 初期 $100.00 (+602.01%)
- 確定: 4575件 (Win 1391 / Loss 1500 / Flat 1684) / skip 4581件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STX/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $702.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.51** / 初期 $100.00 (+55.51%)
- 確定: 1977件 (Win 536 / Loss 473 / Flat 968) / skip 4029件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0347 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $155.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.47** / 初期 $100.00 (+15.47%)
- 確定: 1925件 (Win 564 / Loss 732 / Flat 629) / pending 5件 / skip 2137件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000201 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STX/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $115.47

## 6. Latest Market Context

- 更新: 2026-08-25T10:21:13.617513+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=79339.9
- Funnel: target 1023 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +76.58% | $4,748,497.65 |
| JIMOTHY/USDT:USDT | +58.02% | $1,319,088.39 |
| TAC/USDT:USDT | +39.44% | $6,188,864.98 |
| ONG/USDT:USDT | +36.18% | $7,304,625.70 |
| BR/USDT:USDT | +18.24% | $3,414,041.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAC/USDT:USDT | below_1h_threshold | +3.85% | +3.62% |
| H/USDT:USDT | below_1h_threshold | +3.25% | +3.03% |
| SNXX/USDT:USDT | below_1h_threshold | +3.01% | +2.79% |
| SOXL/USDT:USDT | below_1h_threshold | +2.03% | +1.80% |
| ONG/USDT:USDT | below_1h_threshold | +1.92% | +1.69% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
