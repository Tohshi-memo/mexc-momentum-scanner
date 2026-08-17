# Decision Report

- generated_at: 2026-08-17T15:51:31.539138+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11841**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11841, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.42% | **-1.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +3.92% | **+1.18%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | +1.77% | **+1.06%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.57% | **+2.44%** |
| MARKET_LONG | 20/20 | 100.0% | +1.84% | **+1.84%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.37% | **+1.37%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +1.89% | **+0.57%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +1.13% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 186件 (TP 72 / SL 109 / EXP 5)
- 最新: BR/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$617.79** / 初期 $100.00 (+517.79%)
- 確定: 4185件 (Win 1292 / Loss 1364 / Flat 1529) / skip 4217件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $617.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1818件 (Win 502 / Loss 427 / Flat 889) / skip 3434件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0049 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIO/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.12% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.53** / 初期 $100.00 (+17.53%)
- 確定: 1679件 (Win 504 / Loss 641 / Flat 534) / pending 0件 / skip 1636件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000099 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AIO/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $117.53

## 6. Latest Market Context

- 更新: 2026-08-17T15:51:18.094180+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.43% price=64148.3
- Funnel: target 992 → liquid 180 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +128.87% | $5,704,476.22 |
| GPS/USDT:USDT | +52.06% | $25,942,187.91 |
| TUT/USDT:USDT | +33.94% | $12,087,376.69 |
| STAR/USDT:USDT | +33.10% | $1,086,806.09 |
| ACE/USDT:USDT | +30.63% | $31,933,890.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AEON1/USDT:USDT | below_1h_threshold | +4.33% | +3.90% |
| KORU/USDT:USDT | below_1h_threshold | +3.73% | +3.30% |
| VVV/USDT:USDT | below_1h_threshold | +3.49% | +3.06% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +3.48% | +3.04% |
| SNXX/USDT:USDT | below_1h_threshold | +3.01% | +2.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
