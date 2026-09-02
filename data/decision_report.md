# Decision Report

- generated_at: 2026-09-02T19:56:27.444792+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13375**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13375, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.81% | **-2.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +3.77% | **+0.94%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_4PCT | 18/20 | 90.0% | +0.22% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +7.64% | **+5.73%** |
| MARKET_LONG | 20/20 | 100.0% | +2.21% | **+2.21%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +3.88% | **+2.14%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +2.22% | **+1.77%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +3.32% | **+1.33%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 198件 (TP 74 / SL 119 / EXP 5)
- 最新: FONE/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$882.23** / 初期 $100.00 (+782.23%)
- 確定: 4988件 (Win 1513 / Loss 1633 / Flat 1842) / skip 4948件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $882.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$186.52** / 初期 $100.00 (+86.52%)
- 確定: 2354件 (Win 665 / Loss 565 / Flat 1124) / skip 4432件
- 成長率目線: 平均log +0.000265 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.2023 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $186.52

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.78** / 初期 $100.00 (+14.78%)
- 確定: 2093件 (Win 611 / Loss 819 / Flat 663) / pending 0件 / skip 2755件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000546 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.78

## 6. Latest Market Context

- 更新: 2026-09-02T19:56:15.860636+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=77128.9
- Funnel: target 1044 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +80.17% | $32,803,860.85 |
| BONER/USDT:USDT | +27.54% | $3,071,167.50 |
| BULLA/USDT:USDT | +17.03% | $2,381,569.69 |
| BTW/USDT:USDT | +12.99% | $6,224,113.59 |
| MARSCOIN/USDT:USDT | +9.72% | $3,115,845.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DELLSTOCK/USDT:USDT | below_1h_threshold | +4.39% | +4.67% |
| USELESS/USDT:USDT | below_1h_threshold | +3.95% | +4.22% |
| BULLA/USDT:USDT | below_1h_threshold | +3.79% | +4.06% |
| BONER/USDT:USDT | below_1h_threshold | +2.96% | +3.24% |
| BTW/USDT:USDT | below_1h_threshold | +2.95% | +3.22% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
