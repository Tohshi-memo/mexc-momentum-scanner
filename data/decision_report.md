# Decision Report

- generated_at: 2026-11-20T10:31:30.572496+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19239**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19239, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.08% | **-0.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +3.99% | **+0.40%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.68% | **+0.34%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| MARKET | 20/20 | 100.0% | -0.08% | **-0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.82% | **+0.64%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.58% | **+0.26%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.34% | **+0.18%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.15% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 282件 (TP 102 / SL 172 / EXP 8)
- 最新: KORU/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,701.37** / 初期 $100.00 (+1601.37%)
- 確定: 7386件 (Win 2122 / Loss 2378 / Flat 2886) / skip 8414件
- 成長率目線: 平均log +0.000384 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HUMA/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $1,701.37

## 4. Robust Adaptive DryRun ($100)

- 残高: **$440.26** / 初期 $100.00 (+340.26%)
- 確定: 5063件 (Win 1351 / Loss 1087 / Flat 2625) / skip 7587件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0003 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PIPPIN/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $440.26

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7399件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000168 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-20T10:31:20.040021+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.53% price=61938.0
- Funnel: target 1084 → liquid 159 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.8 >= 65=1, 4h RSI 69.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CYBER/USDT:USDT | +35.93% | $1,417,480.80 |
| SOXS/USDT:USDT | +21.25% | $61,778,483.47 |
| BTW/USDT:USDT | +17.36% | $4,588,071.69 |
| UVXY/USDT:USDT | +12.86% | $4,101,024.80 |
| PIPPIN/USDT:USDT | +11.77% | $1,196,801.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ICNT/USDT:USDT | below_1h_threshold | +4.27% | +3.74% |
| BLESS/USDT:USDT | below_1h_threshold | +3.87% | +3.34% |
| SOXS/USDT:USDT | below_1h_threshold | +3.79% | +3.25% |
| UVXY/USDT:USDT | below_1h_threshold | +3.42% | +2.89% |
| RAVE/USDT:USDT | below_1h_threshold | +3.21% | +2.67% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
