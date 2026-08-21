# Decision Report

- generated_at: 2026-08-21T01:41:27.027375+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12119**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12119, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 6/20 | 30.0% | +5.28% | **+1.59%** |
| LIMIT_9PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_10PCT | 3/20 | 15.0% | +7.15% | **+1.07%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +3.81% | **+0.95%** |
| LIMIT_7PCT | 6/20 | 30.0% | +2.54% | **+0.76%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.76% | **+1.24%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.42% | **+0.97%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.72% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$656.69** / 初期 $100.00 (+556.69%)
- 確定: 4330件 (Win 1329 / Loss 1417 / Flat 1584) / skip 4350件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $656.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1822件 (Win 502 / Loss 429 / Flat 891) / skip 3708件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1344 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $154.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.86** / 初期 $100.00 (+17.86%)
- 確定: 1804件 (Win 536 / Loss 683 / Flat 585) / pending 6件 / skip 1783件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000226 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $117.86

## 6. Latest Market Context

- 更新: 2026-08-21T01:41:15.583698+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +1.25% price=74606.3
- Funnel: target 1011 → liquid 195 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=44, below_relative_strength=3, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.7 >= 65=1, 4h RSI 85.3 >= 65=1, 4h RSI 69.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ONG/USDT:USDT | +86.93% | $25,188,305.03 |
| CATE/USDT:USDT | +77.45% | $3,687,422.11 |
| ONT/USDT:USDT | +23.81% | $3,417,501.21 |
| ENA/USDT:USDT | +17.45% | $49,380,979.64 |
| TUT/USDT:USDT | +10.79% | $5,776,772.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COLLECT/USDT:USDT | below_relative_strength | +5.75% | +4.49% |
| NEIROCTO/USDT:USDT | below_relative_strength | +5.67% | +4.42% |
| ONT/USDT:USDT | below_relative_strength | +5.38% | +4.12% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +4.19% | +2.94% |
| KORU/USDT:USDT | below_1h_threshold | +3.75% | +2.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
