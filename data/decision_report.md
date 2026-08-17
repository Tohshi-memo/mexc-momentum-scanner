# Decision Report

- generated_at: 2026-08-17T15:36:36.018191+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11840**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11840, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.42% | **-1.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 11/20 | 55.0% | +1.98% | **+1.09%** |
| LIMIT_6PCT | 5/20 | 25.0% | +4.33% | **+1.08%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.87% | **+0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.57% | **+2.44%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +2.26% | **+2.26%** |
| MARKET_LONG | 20/20 | 100.0% | +1.44% | **+1.44%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.30% | **+0.78%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +1.66% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 186件 (TP 72 / SL 109 / EXP 5)
- 最新: BR/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$617.79** / 初期 $100.00 (+517.79%)
- 確定: 4185件 (Win 1292 / Loss 1364 / Flat 1529) / skip 4216件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $617.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1818件 (Win 502 / Loss 427 / Flat 889) / skip 3433件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0025 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIO/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.12% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.53** / 初期 $100.00 (+17.53%)
- 確定: 1679件 (Win 504 / Loss 641 / Flat 534) / pending 0件 / skip 1635件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000099 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AIO/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $117.53

## 6. Latest Market Context

- 更新: 2026-08-17T15:36:23.317713+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=64007.5
- Funnel: target 992 → liquid 179 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +141.50% | $5,573,910.60 |
| GPS/USDT:USDT | +52.88% | $25,753,495.48 |
| ACE/USDT:USDT | +35.93% | $31,372,272.73 |
| STAR/USDT:USDT | +34.48% | $1,070,182.28 |
| TUT/USDT:USDT | +32.29% | $11,544,223.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AEON1/USDT:USDT | below_1h_threshold | +4.31% | +4.09% |
| KORU/USDT:USDT | below_1h_threshold | +3.73% | +3.52% |
| SNXX/USDT:USDT | below_1h_threshold | +3.01% | +2.80% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +2.57% | +2.36% |
| NIULAI/USDT:USDT | below_1h_threshold | +2.46% | +2.25% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
