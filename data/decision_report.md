# Decision Report

- generated_at: 2026-08-26T09:51:32.188624+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12691**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12691, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +0.67% | **+0.34%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.70% | **+2.43%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.99% | **+2.24%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.10% | **+1.55%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +1.43% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$710.24** / 初期 $100.00 (+610.24%)
- 確定: 4593件 (Win 1398 / Loss 1507 / Flat 1688) / skip 4659件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TAC/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $710.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$159.59** / 初期 $100.00 (+59.59%)
- 確定: 1988件 (Win 542 / Loss 474 / Flat 972) / skip 4114件
- 成長率目線: 平均log +0.000235 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1710 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TAC/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $159.59

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.93** / 初期 $100.00 (+16.93%)
- 確定: 1967件 (Win 578 / Loss 748 / Flat 641) / pending 6件 / skip 2195件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000514 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TAC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $116.93

## 6. Latest Market Context

- 更新: 2026-08-26T09:51:22.403635+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.35% price=78400.3
- Funnel: target 1022 → liquid 170 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.5 >= 65=1, 4h RSI 67.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +172.58% | $12,866,236.61 |
| BMT/USDT:USDT | +51.76% | $13,998,943.70 |
| TAC/USDT:USDT | +49.69% | $6,084,442.44 |
| LONGXIA/USDT:USDT | +24.78% | $1,964,656.16 |
| PORTAL/USDT:USDT | +20.21% | $4,002,167.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +1.75% | +2.10% |
| PORTAL/USDT:USDT | below_1h_threshold | +1.62% | +1.97% |
| CHIP/USDT:USDT | below_1h_threshold | +1.33% | +1.68% |
| BEAT/USDT:USDT | below_1h_threshold | +1.17% | +1.52% |
| HEI/USDT:USDT | below_1h_threshold | +0.76% | +1.11% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
