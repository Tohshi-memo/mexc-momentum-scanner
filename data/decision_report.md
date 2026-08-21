# Decision Report

- generated_at: 2026-08-21T02:51:30.755888+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12132**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12132, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.41% | **-2.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 6/20 | 30.0% | +3.95% | **+1.19%** |
| LIMIT_ATR | 16/20 | 80.0% | +1.40% | **+1.12%** |
| LIMIT_BB3S | 2/19 | 10.5% | +8.00% | **+0.84%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_9PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +6.21% | **+3.41%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +4.59% | **+2.07%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.70% | **+1.48%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.54% | **+1.46%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.77% | **+1.32%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$665.71** / 初期 $100.00 (+565.71%)
- 確定: 4343件 (Win 1335 / Loss 1424 / Flat 1584) / skip 4350件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $665.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1822件 (Win 502 / Loss 429 / Flat 891) / skip 3721件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0967 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $154.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.03** / 初期 $100.00 (+18.03%)
- 確定: 1817件 (Win 540 / Loss 687 / Flat 590) / pending 5件 / skip 1784件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000229 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $118.03

## 6. Latest Market Context

- 更新: 2026-08-21T02:51:21.123953+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.87% price=74448.0
- Funnel: target 1011 → liquid 193 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.4 >= 65=1, 4h RSI 87.8 >= 65=1, 4h RSI 82.6 >= 65=1, 4h RSI 71.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ONG/USDT:USDT | +102.14% | $30,720,093.36 |
| CATE/USDT:USDT | +101.14% | $4,232,774.14 |
| ONT/USDT:USDT | +27.20% | $3,587,048.85 |
| ENA/USDT:USDT | +20.55% | $53,034,394.88 |
| PEOPLE/USDT:USDT | +13.95% | $4,376,367.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BOME/USDT:USDT | below_1h_threshold | +4.24% | +5.11% |
| ONT/USDT:USDT | below_1h_threshold | +3.96% | +4.83% |
| NIULAI/USDT:USDT | below_1h_threshold | +3.66% | +4.53% |
| MAGMA/USDT:USDT | below_1h_threshold | +2.82% | +3.69% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +2.73% | +3.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
