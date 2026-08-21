# Decision Report

- generated_at: 2026-08-21T02:06:22.413885+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12122**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12122, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +4.74% | **+1.19%** |
| LIMIT_10PCT | 3/20 | 15.0% | +7.15% | **+1.07%** |
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +3.14% | **+0.94%** |
| LIMIT_3PCT | 18/20 | 90.0% | +0.85% | **+0.76%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.76% | **+1.24%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.21% | **+0.88%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.01% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$654.24** / 初期 $100.00 (+554.24%)
- 確定: 4333件 (Win 1330 / Loss 1419 / Flat 1584) / skip 4350件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONG/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $654.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1822件 (Win 502 / Loss 429 / Flat 891) / skip 3711件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1077 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $154.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.06** / 初期 $100.00 (+18.06%)
- 確定: 1807件 (Win 537 / Loss 683 / Flat 587) / pending 5件 / skip 1783件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000206 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ONG/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $118.06

## 6. Latest Market Context

- 更新: 2026-08-21T02:06:12.028175+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.30% price=74880.0
- Funnel: target 1011 → liquid 192 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +74.01% | $3,791,470.49 |
| ONG/USDT:USDT | +56.06% | $27,976,683.43 |
| ONT/USDT:USDT | +19.16% | $3,446,598.71 |
| ENA/USDT:USDT | +19.10% | $51,367,108.54 |
| NIULAI/USDT:USDT | +14.37% | $6,441,630.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EYE/USDT:USDT | below_1h_threshold | +3.08% | +3.38% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +2.73% | +3.03% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +2.57% | +2.87% |
| KORU/USDT:USDT | below_1h_threshold | +2.41% | +2.70% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +2.22% | +2.52% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
