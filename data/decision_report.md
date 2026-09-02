# Decision Report

- generated_at: 2026-09-02T11:26:21.174586+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13331**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13331, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.29% | **-0.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +2.48% | **+0.37%** |
| LIMIT_BB3S | 10/18 | 55.6% | +0.45% | **+0.25%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.17% | **+0.13%** |
| LIMIT_ATR | 10/20 | 50.0% | -0.03% | **-0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.17% | **+0.97%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.24% | **+0.80%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.56% | **+0.50%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.43% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 198件 (TP 74 / SL 119 / EXP 5)
- 最新: FONE/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$831.77** / 初期 $100.00 (+731.77%)
- 確定: 4957件 (Win 1504 / Loss 1628 / Flat 1825) / skip 4935件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: T/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $831.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$174.85** / 初期 $100.00 (+74.85%)
- 確定: 2310件 (Win 642 / Loss 553 / Flat 1115) / skip 4432件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0176 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: T/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $174.85

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.78** / 初期 $100.00 (+14.78%)
- 確定: 2093件 (Win 611 / Loss 819 / Flat 663) / pending 0件 / skip 2708件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000167 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.78

## 6. Latest Market Context

- 更新: 2026-09-02T11:26:08.822737+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.35% price=76372.0
- Funnel: target 1044 → liquid 159 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| T/USDT:USDT | +47.66% | $4,652,438.35 |
| MAGMA/USDT:USDT | +43.04% | $9,698,066.91 |
| FONE/USDT:USDT | +39.47% | $1,831,913.63 |
| CASHCAT/USDT:USDT | +16.85% | $1,857,714.92 |
| UAI/USDT:USDT | +16.50% | $27,162,382.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FF/USDT:USDT | below_1h_threshold | +2.14% | +2.49% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.92% | +2.27% |
| FLOCK/USDT:USDT | below_1h_threshold | +1.48% | +1.83% |
| BTW/USDT:USDT | below_1h_threshold | +1.21% | +1.56% |
| XPD/USDT:USDT | below_1h_threshold | +0.78% | +1.13% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
